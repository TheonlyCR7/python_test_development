import pytest
from click.testing import CliRunner
from unittest.mock import mock_open, patch
import json
import app  # 假设上面代码文件名为 app.py

@pytest.fixture
def runner():
    return CliRunner()

def test_load_tasks_empty_file(mocker):
    mocker.patch("builtins.open", mock_open(read_data=""))
    assert app.load_tasks() == []

def test_load_tasks_with_data(mocker):
    data = [{"description": "Test task", "created_at": "2024-01-01T10:00:00"}]
    mocker.patch("builtins.open", mock_open(read_data=json.dumps(data)))
    assert app.load_tasks() == data

def test_save_tasks(mocker):
    mock_file = mock_open()
    mocker.patch("builtins.open", mock_file)
    data = [{"description": "Test task", "created_at": "2024-01-01T10:00:00"}]
    app.save_tasks(data)
    mock_file().write.assert_called_once_with(json.dumps(data))

def test_add_command(runner, mocker):
    mock_save = mocker.patch("app.save_tasks")
    mock_load = mocker.patch("app.load_tasks", return_value=[])
    result = runner.invoke(app.cli, ["add", "Test task"])
    assert result.exit_code == 0
    assert "Task added successfully." in result.output
    mock_save.assert_called_once_with([{"description": "Test task", "created_at": pytest.match(r"2024-\d{2}-\d{2}")}])

def test_list_command_empty(runner, mocker):
    mocker.patch("app.load_tasks", return_value=[])
    result = runner.invoke(app.cli, ["list"])
    assert result.exit_code == 0
    assert "No tasks found." in result.output

def test_list_command_with_tasks(runner, mocker):
    tasks = [{"description": "Test task", "created_at": "2024-01-01T10:00:00"}]
    mocker.patch("app.load_tasks", return_value=tasks)
    result = runner.invoke(app.cli, ["list"])
    assert result.exit_code == 0
    assert "1. Test task (2024-01-01T10:00:00)" in result.output

def test_complete_command_valid_index(runner, mocker):
    tasks = [{"description": "Task to complete", "created_at": "2024-01-01T10:00:00"}]
    mocker.patch("app.load_tasks", return_value=tasks)
    mock_save = mocker.patch("app.save_tasks")
    result = runner.invoke(app.cli, ["complete", "1"])
    assert result.exit_code == 0
    assert 'Task "Task to complete" completed successfully.' in result.output
    mock_save.assert_called_once_with([])

def test_complete_command_invalid_index(runner, mocker):
    mocker.patch("app.load_tasks", return_value=[])
    result = runner.invoke(app.cli, ["complete", "1"])
    assert result.exit_code == 0
    assert "Invalid task index." in result.output
