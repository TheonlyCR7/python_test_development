YAML 是 "YAML Ain't a Markup Language"（YAML 不是一种标记语言）的递归缩写。在开发的这种语言时，YAML 的意思其实是："Yet Another Markup Language"（仍是一种标记语言）。

YAML 的配置文件后缀为 .yml，如：**runoob.yml** 。

## 基本语法

- 大小写敏感
- 使用缩进表示层级关系
- 缩进不允许使用tab，只允许空格
- 缩进的空格数不重要，只要相同层级的元素左对齐即可
- '#'表示注释



## 数据类型

YAML 支持以下几种数据类型：

- 对象：键值对的**集合**（也就是说可能是一组键值对），又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）

  ```
  id: 1
  name: company1
  price: 200W
  ```

- 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）

  ```
  - A
  - B
  - C
  ```

- 纯量（scalars）：单个的、不可再分的值

  ```
  boolean: 
      - TRUE  #true,True都可以
      - FALSE  #false，False都可以
  ```

* 复合结构

  ```
  languages:
    - Ruby
    - Perl
    - Python
  websites:
    YAML: yaml.org 
    Ruby: ruby-lang.org 
    Python: python.org 
    Perl: use.perl.org
  ```

* 引用

  & 锚点和 * 别名，可以用来引用



