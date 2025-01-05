

## **Python pytest 框架系统梳理**

### **1. pytest 简介**

- 一个功能强大的 Python 测试框架，比 `unittest` 更加简洁和易用。
- 主要特点：
  - 自动发现测试用例。
  - 支持简单断言。
  - 丰富的插件生态。
  - 支持参数化测试。

------

### **2. 安装 pytest**

使用 pip 安装：

```bash
pip install pytest
```

------

### **3. 基本用法**

#### **3.1 测试文件与函数**

- 测试文件：文件名以 `test_` 或 `_test` 开头/结尾。
- 测试函数：函数名以 `test_` 开头。

示例：

```python
# test_sample.py
def test_sum():
    assert sum([1, 2, 3]) == 6

def test_difference():
    assert 5 - 3 == 2
```

#### **3.2 运行测试**

在命令行运行：

```bash
pytest           # 运行当前目录下所有测试
pytest test_sample.py  # 运行指定文件
pytest test_sample.py::test_sum  # 运行指定测试函数
```

------

### **4. 断言方法**

pytest 使用 Python 的内置断言 (`assert`) 语句，语法更加直观。

示例：

```python
def test_assert_examples():
    assert 1 + 1 == 2
    assert "pytest" in "learn pytest framework"
    assert [1, 2, 3] == [1, 2, 3]
```

**断言失败时的提示信息**：

```python
def test_fail():
    assert 1 == 2  # 报错信息：assert 1 == 2
```

------

### **5. pytest 功能详解**

#### **5.1 setup 和 teardown**

- 模块级别：
  - 在模块开始前/后执行一次：`setup_module` 和 `teardown_module`。
- 函数级别：
  - 在每个测试函数开始前/后执行：`setup_function` 和 `teardown_function`。

示例：

```python
def setup_function():
    print("Setup before test")

def teardown_function():
    print("Teardown after test")

def test_example():
    assert True
```

- 类级别（setup_class和 teardown_class）：

  - 在类中所有测试开始前/后执行。

  - 方法级别

    （setup_method和 teardown_method）：

    - 在类中每个测试方法开始前/后执行。

#### **5.2 使用 fixture**

- pytest 提供了 `fixture` 装饰器，用于实现测试的前置条件。

示例：

```python
import pytest

@pytest.fixture
def setup_data():
    return {"key": "value"}

def test_fixture_example(setup_data):
    assert setup_data["key"] == "value"
```

- Fixture 支持作用域：
  - `scope="function"`：默认值，每个测试用例调用一次。
  - `scope="module"`：模块范围内共享。
  - `scope="class"`：类范围内共享。
  - `scope="session"`：整个测试会话范围内共享。

#### **5.3 参数化测试**

- 使用 `@pytest.mark.parametrize` 进行参数化测试，减少重复代码。

示例：

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 5, 8)])
def test_addition(a, b, expected):
    assert a + b == expected
```

------

### **6. 测试跳过与条件执行**

#### **6.1 跳过测试**

- 使用 `@pytest.mark.skip` 跳过测试。
- 使用 `@pytest.mark.skipif` 条件跳过。

示例：

```python
import pytest

@pytest.mark.skip(reason="跳过此测试示例")
def test_skip():
    assert False

@pytest.mark.skipif(1 + 1 != 2, reason="条件为真时跳过")
def test_skipif():
    assert True
```

#### **6.2 预期失败**

- 使用 `@pytest.mark.xfail` 标记预期失败的测试。

示例：

```python
@pytest.mark.xfail
def test_xfail():
    assert 1 == 2
```

------

### **7. pytest 插件与扩展**

#### **7.1 pytest-cov**

- 测试覆盖率工具。

- 安装：

  ```bash
  pip install pytest-cov
  ```

- 使用：

  ```bash
  pytest --cov=your_project
  ```

#### **7.2 pytest-html**

- 生成 HTML 格式测试报告。

- 安装：

  ```bash
  pip install pytest-html
  ```

- 使用：

  ```bash
  pytest --html=report.html
  ```

------

### **8. pytest 命令行选项**

| 参数                       | 描述                    |
| -------------------------- | ----------------------- |
| `-v`                       | 显示详细的测试信息      |
| `-q`                       | 显示简洁的测试信息      |
| `--maxfail=n`              | 失败 n 次后停止测试     |
| `--durations=n`            | 显示耗时最长的 n 个测试 |
| `--disable-warnings`       | 禁用警告信息            |
| `--tb=short` / `--tb=long` | 控制 traceback 输出风格 |

示例：

```bash
pytest -v --maxfail=2 --disable-warnings
```

------

### **9. Mock 测试**

与 `unittest.mock` 类似，pytest 可以模拟依赖的对象。

示例：

```python
from unittest.mock import MagicMock

def get_data(source):
    return source.read()

def test_mock_example():
    mock_source = MagicMock()
    mock_source.read.return_value = "mock data"
    result = get_data(mock_source)
    assert result == "mock data"
```

------

### **10. 实践建议**

1. 命名规范：
   - 测试文件名以 `test_` 开头。
   - 测试函数名以 `test_` 开头。
2. 简洁的测试：
   - 避免复杂的测试逻辑，保持测试简单明了。
3. 隔离测试环境：
   - 使用 `fixture` 和 `mock` 隔离测试依赖。
4. 覆盖率检查：
   - 使用 `pytest-cov` 检查代码覆盖率。

------

通过以上内容的系统梳理，可以帮助你高效掌握 pytest 框架，进一步提升测试开发能力。