import click
import json
from datetime import datetime

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('description')
def add(description):
    tasks = load_tasks()
    new_task = {'description': description, 'created_at': str(datetime.now())}
    tasks.append(new_task)
    save_tasks(tasks)
    click.echo('Task added successfully.')

@cli.command()
def list():
    tasks = load_tasks()
    if len(tasks) == 0:
        click.echo('No tasks found.')
    else:
        for index, task in enumerate(tasks):
            click.echo(f'{index + 1}. {task["description"]} ({task["created_at"]})')

@cli.command()
@click.argument('task_index', type=int)
def complete(task_index):
    tasks = load_tasks()
    if task_index < 1 or task_index > len(tasks):
        click.echo('Invalid task index.')
    else:
        completed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        click.echo(f'Task "{completed_task["description"]}" completed successfully.')

if __name__ == '__main__':
    cli()
