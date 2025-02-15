



## 关于pytest.ini文件中的标记和冒烟规则

* 你提供的 `pytest` 配置文件中有一个标记（`markers`）配置项，其中定义了两个标记：

  - `smoke`：表示“冒烟用例”
  - `product_manage`：表示“商品管理”

  ### 冒烟测试（Smoke Test）

  **冒烟测试**是一种软件测试的基本形式，用来验证软件系统的核心功能是否正常。它通常是在进行新版本发布或者大规模修改后，进行的一项初步测试，以确保软件的基本功能没有受到影响。

  “冒烟”这个名字来源于硬件的测试过程，通常是在测试硬件时，如果设备启动时没有冒烟，那就可以进行进一步的测试。在软件开发中，冒烟测试也是类似的概念：首先检查系统的基础功能是否能正常工作。如果冒烟测试通过，才能进行更深入的功能测试。

  ### 在 `pytest` 中使用标记

  在 `pytest` 中，标记可以用来分类测试用例。你可以通过命令行指定要运行的标记，或者在测试用例中指定某些标记以便于选择性执行。

  #### 举个例子，如何在 `pytest` 中使用 `smoke` 标记：

  1. 在测试函数或者类上加上 `@pytest.mark.smoke` 标记：

     ```python
     import pytest
     
     @pytest.mark.smoke
     def test_login():
         assert True
     ```

  2. 在运行测试时，通过 `-m` 参数选择只运行 `smoke` 标记的测试：

     ```bash
     pytest -m smoke
     ```

  这样，只有带有 `smoke` 标记的测试用例会被执行。这对于你想只运行冒烟测试的情况非常有用。

  ### 在你的配置文件中：

  你在 `pytest.ini` 配置文件中定义了两个标记：

  ```ini
  markers =
      smoke: 冒烟用例
      product_manage: 商品管理
  ```

  这表示你可以将这些标记应用到测试用例上，方便后续通过标记筛选出不同类别的测试用例，进行不同的测试。

  比如：

  ```python
  import pytest
  
  @pytest.mark.smoke
  def test_basic_functionality():
      # 测试基础功能
      pass
  
  @pytest.mark.product_manage
  def test_product_addition():
      # 测试商品添加功能
      pass
  ```

  ### 总结

  - **冒烟测试**是确保系统最基本功能正常的初步测试。
  - 通过 `pytest` 的标记功能，你可以分类、选择性地运行某些类别的测试用例，比如只执行“冒烟用例”或者“商品管理”相关的测试。

  如果你有任何其他问题或需要进一步解释，随时告诉我！