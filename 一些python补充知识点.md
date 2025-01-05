## "".join()

**作用**：将一个字符列表拼接成字符串。

`join()` 是字符串的方法，用来将列表中的元素用指定的分隔符连接成一个字符串。

**语法**：

```
"用户指定的分隔符".join(可迭代对象)
",".join(strs)
```



## 关于哈希的语法

**Python中哈希的知识点和语法**

哈希（Hashing）是一种通过特定算法将数据映射为固定长度的值（称为哈希值或散列值）的技术。Python中，哈希的主要应用场景包括字典（`dict`）、集合（`set`）、哈希函数（`hash()`）、以及相关的数据结构（如哈希表）。

---

**哈希的基本知识**

1. **哈希函数**：
   - 哈希函数是一个将输入数据映射为固定长度值的函数。
   - Python 提供了内置的哈希函数 `hash()`，用于生成对象的哈希值。
   - 哈希值的特点：
     - 相同输入的哈希值总是相同（确定性）。
     - 哈希值是整数。
     - 哈希值可能存在冲突（不同输入映射为相同哈希值）。

2. **可哈希对象**：
   - 在 Python 中，只有**不可变对象**是可哈希的，例如：
     - 数字类型：`int`, `float`
     - 字符串：`str`
     - 元组：`tuple`（但元组中包含的元素也必须是不可变的）。
   - **不可哈希对象**：`list`, `dict`, `set` 等可变类型。
   - 可哈希对象在字典的键（`key`）或集合的元素中使用。

3. **哈希表**：
   - 哈希表是存储键值对的数据结构，用于快速查找、插入和删除操作。
   - 在 Python 中，字典和集合是基于哈希表实现的。
     - 字典（`dict`）：键必须是可哈希的，值可以是任意类型。
     - 集合（`set`）：集合中的元素必须是可哈希的。

---

**Python中的哈希相关语法**

1. **`hash()` 函数**

`hash()` 是一个内置函数，用于计算对象的哈希值。

- **语法**：
  ```python
  hash(object)
  ```
- **参数**：`object` 必须是一个可哈希对象（不可变类型）。
- **返回值**：一个整数，表示对象的哈希值。

**示例**：
```python
print(hash(42))        # 输出：42
print(hash("hello"))   # 输出：哈希值（整数，因实现不同而不同）
print(hash((1, 2, 3))) # 输出：对应元组的哈希值
```

**注意**：
- 可变对象如列表会报错：
  ```python
  hash([1, 2, 3])  # 报错：TypeError: unhashable type: 'list'
  ```

---

2. **字典（`dict`）**

字典的键必须是可哈希的对象。

- **创建字典**：
  ```python
  my_dict = {"key1": "value1", "key2": "value2"}
  print(my_dict["key1"])  # 输出：value1
  ```

- **使用不可哈希对象作为键会报错**：
  ```python
  my_dict = {[1, 2]: "value"}  # 报错：TypeError: unhashable type: 'list'
  ```

---

3. **集合（`set`）**

集合的元素必须是可哈希的对象。

- **创建集合**：
  ```python
  my_set = {1, 2, 3, "hello"}
  print(my_set)  # 输出：{1, 2, 3, 'hello'}
  ```

- **不可哈希对象会报错**：
  ```python
  my_set = {[1, 2], (3, 4)}  # 报错：TypeError: unhashable type: 'list'
  ```

---

4. **`collections.defaultdict`**

`defaultdict` 是 `dict` 的一种变体，提供默认值功能，常用于处理哈希表的默认分组。

**示例**：
```python
import collections

# 创建一个默认值为列表的哈希表
hash_table = collections.defaultdict(list)

hash_table["key1"].append(10)
hash_table["key1"].append(20)
print(hash_table)  # 输出：defaultdict(<class 'list'>, {'key1': [10, 20]})
```

---

#### 5. **检查对象是否可哈希**

可以通过尝试调用 `hash()` 或检查 `__hash__` 方法来判断对象是否可哈希。

**示例**：
```python
print(hash("hello"))  # 输出哈希值，字符串是可哈希的
print(hash((1, 2)))   # 输出哈希值，元组是可哈希的

try:
    hash([1, 2, 3])   # 报错，列表不可哈希
except TypeError as e:
    print(e)          # 输出错误信息
```

---

**哈希表的应用场景**

1. **快速查找**：
   - 使用哈希表可以在 \(O(1)\) 时间内完成插入、删除和查找操作。
   - 例如字典和集合的操作。

2. **数据分组**：
   - 使用 `defaultdict` 或哈希表键值对分组数据。
   - 应用场景：字母异位词分组、单词计数。

3. **去重**：
   - 使用集合快速去重，基于哈希值判断元素是否重复。

4. **缓存机制**：
   - 利用哈希表实现快速缓存，例如 LRU 缓存。

---

**注意事项**

1. **哈希冲突**：
   - 不同对象可能有相同的哈希值（称为哈希冲突）。
   - Python 的字典和集合通过开放寻址或链地址法解决冲突。

2. **哈希值的不可变性**：
   - 对于相同的输入，`hash()` 的输出在程序的同一次运行中不会改变。
   - 但是跨 Python 版本或不同系统，`hash()` 的结果可能不同。

3. **自定义类的哈希值**：
   - 如果需要自定义类作为字典键或集合元素，需实现 `__hash__` 和 `__eq__` 方法。

**示例**：
```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)  # 基于属性生成哈希值

    def __eq__(self, other):
        return self.value == other.value

obj1 = MyClass(10)
obj2 = MyClass(10)
print(hash(obj1) == hash(obj2))  # 输出：True
print(obj1 == obj2)             # 输出：True
```

---

**总结**

1. 哈希在 Python 中广泛应用于字典和集合等数据结构，提供高效的查找性能。
2. 理解可哈希对象的概念，避免在字典键或集合元素中使用不可哈希对象。
3. 学习使用 `hash()`、`collections.defaultdict` 等工具，可以快速构建基于哈希的解决方案。







## 类方法

类方法是绑定到类本身的方法，它的第一个参数是类本身（通常使用 `cls` 来表示）。类方法可以通过类名或实例调用。类方法通常用于修改类属性，或者作为工厂方法返回类的不同实例。

定义类方法时，使用 `@classmethod` 装饰器。类方法的常见用途包括修改类属性和定义工厂方法。

示例：

```python
class MyClass:
    class_attribute = "I am a class attribute"
    
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute
    
    @classmethod
    def update_class_attribute(cls, new_value):
        cls.class_attribute = new_value

    @classmethod
    def create_instance(cls, instance_attribute):
        return cls(instance_attribute)

# 通过类方法修改类属性
MyClass.update_class_attribute("Updated class attribute")
print(MyClass.class_attribute)

# 通过类方法创建实例
obj = MyClass.create_instance("Instance attribute")
print(obj.instance_attribute)
```

## 类属性

类属性是属于类的属性，而不是属于类的实例。所有类的实例共享同一个类属性。类属性通常用于存储对所有实例通用的数据，例如常量或配置信息。类属性可以通过类名或实例访问，但如果通过实例修改类属性，实际上是在实例中创建了一个新的实例属性，而不是修改类属性。

定义类属性时，通常在类体内部直接赋值。

示例：

```python
class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

# 访问类属性
print(MyClass.class_attribute)

# 创建实例并访问类属性
obj = MyClass("Instance attribute")
print(obj.class_attribute)

# 修改类属性
MyClass.class_attribute = "Updated class attribute"
print(MyClass.class_attribute)
print(obj.class_attribute)  # 类属性的修改会影响所有实例
```

### 类属性与实例属性的区别

- **类属性**：属于类本身，所有实例共享这个属性。可以通过类名或实例来访问，但建议使用类名访问。
- **实例属性**：属于实例，每个实例可以有不同的实例属性。实例属性在实例创建时定义。

示例：通过实例修改类属性

```python
class MyClass:
    class_attribute = "I am a class attribute"

# 创建实例
obj = MyClass("Instance attribute")

# 通过实例修改类属性
obj.class_attribute = "Instance specific value"

print(obj.class_attribute)  # 会访问实例属性
print(MyClass.class_attribute)  # 仍然是类级别的属性
```

### 总结

1. 类方法

   ：

   - 使用 `@classmethod` 装饰器。
   - 第一个参数是 `cls`，表示类本身。
   - 类方法可以通过类名或实例名调用，通常用于修改类属性或创建实例。

2. 类属性

   ：

   - 属于类本身，所有实例共享。
   - 可以通过类名访问，也可以通过实例访问，但修改类属性时建议使用类名。
   - 实例可以覆盖类属性，但不会影响类级别的属性。

类方法和类属性通常一起使用，尤其是在需要对类的共享状态进行管理或初始化时。

------

这个版本已经完全去除了所有的 `#` 符号。如果您有任何其他问题，请随时告诉我！



## 类属性

在 Python 中，类属性是属于类本身的属性，而不是属于类的实例。类属性可以被类的所有实例共享，并且它们通常用于存储类级别的数据。类属性通过类名访问，也可以通过实例访问，但修改类属性会影响所有实例的值（如果实例没有覆盖该属性）。

类属性的定义

类属性是在类的内部定义的变量，通常在类体内直接赋值。

示例：

```python
class MyClass:
    class_attribute = "I am a class attribute"
    
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

print(MyClass.class_attribute)

obj = MyClass("I am an instance attribute")

print(obj.instance_attribute)

print(obj.class_attribute)
```

类属性与实例属性

- **类属性**：属于类本身，并且所有实例共享该属性。可以通过类名或实例名访问。
- **实例属性**：属于特定的实例，通常通过实例访问。

修改类属性

类属性可以直接通过类名进行修改，也可以通过实例进行修改，但是推荐使用类名来修改，因为如果通过实例修改类属性，实际上是在该实例中创建了一个新的实例属性，而不是修改类属性。

示例：

```python
class MyClass:
    class_attribute = "I am a class attribute"

MyClass.class_attribute = "I am the updated class attribute"

print(MyClass.class_attribute)

obj1 = MyClass()
obj2 = MyClass()

print(obj1.class_attribute)
print(obj2.class_attribute)
```

通过实例修改类属性

如果通过实例修改类属性，它会在实例中创建一个同名的实例属性，遮蔽掉类属性，但不会改变类级别的属性。

```python
class MyClass:
    class_attribute = "I am a class attribute"

obj = MyClass()

obj.class_attribute = "I am the instance attribute"

print(obj.class_attribute)

print(MyClass.class_attribute)
```

使用 `@classmethod` 修改类属性

有时我们可能需要通过类方法来修改类属性。此时可以使用 `@classmethod` 装饰器来定义一个类方法，通过 `cls` 参数来修改类属性。

示例：

```python
class MyClass:
    class_attribute = "I am a class attribute"
    
    @classmethod
    def update_class_attribute(cls, new_value):
        cls.class_attribute = new_value

MyClass.update_class_attribute("I am the updated class attribute")

print(MyClass.class_attribute)
```

总结

1. 类属性是属于类本身的，而非某个实例。
2. 类属性可以通过类名或实例访问，但推荐通过类名访问。
3. 修改类属性时，最好通过类名进行修改，不要通过实例修改，除非你想在实例中覆盖类属性。
4. 可以使用类方法修改类属性。

类属性通常用于存储那些所有实例共享的数据，例如类的配置项或常量。



类属性的定义方式

类属性并不一定非要使用 `cls.name` 来定义，通常类属性是在类体内定义的，但它的访问和修改方式可能不同。您提到的 `cls.name` 主要是类方法中通过 `cls` 来访问类属性的一种方式。而类属性本身通常是直接在类定义时定义的，不需要在类方法中使用 `cls` 来定义。

### 类属性定义的常见方式

类属性通常在类的定义体内直接赋值。你可以通过类名或实例来访问类属性。

示例 1：直接定义类属性

```python
class MyClass:
    # 直接在类体内定义类属性
    class_attribute = "I am a class attribute"

# 通过类名访问类属性
print(MyClass.class_attribute)  # 输出 "I am a class attribute"

# 创建实例
obj = MyClass()

# 通过实例访问类属性
print(obj.class_attribute)  # 输出 "I am a class attribute"
```

示例 2：通过类方法定义类属性

类方法通常用于修改类属性，而不是定义类属性。定义类属性时，直接在类体内定义即可。类方法可以用来修改类属性。

```python
class MyClass:
    # 直接定义类属性
    class_attribute = "I am a class attribute"
    
    @classmethod
    def update_class_attribute(cls, new_value):
        cls.class_attribute = new_value 
        # 通过cls标识来表示是对类属性进行修改和操作
        # 这个标识只有在类方法中才有用

# 通过类方法修改类属性
MyClass.update_class_attribute("Updated class attribute")
print(MyClass.class_attribute)  # 输出 "Updated class attribute"
```

类属性不需要使用 `cls` 定义

类属性是属于类的，而不是属于类的实例，因此它不需要在类方法中通过 `cls` 来定义。类属性通常是直接在类的定义中定义的，`cls` 更多用于类方法中来访问或修改类属性，而不用于定义类属性。

示例 3：通过实例修改类属性

虽然类属性通常通过类来访问，但实例也可以访问类属性。如果实例通过同名的属性修改类属性，实际上它会创建一个实例属性，遮蔽掉类属性。也就是说，实例可以修改类属性，但这种修改只会影响实例本身，不会影响其他实例或类本身。

```python
class MyClass:
    # 直接定义类属性
    class_attribute = "I am a class attribute"

# 创建实例
obj = MyClass()

# 实例访问类属性
print(obj.class_attribute)  # 输出 "I am a class attribute"

# 通过实例修改类属性
obj.class_attribute = "I am an instance attribute"
print(obj.class_attribute)  # 输出 "I am an instance attribute"
```

### 总结

1. **类属性定义**：类属性通常在类体内直接定义，而不是通过类方法中的 `cls` 来定义。它是属于类的属性，所有实例共享。
2. **类方法中的 `cls`**：`cls` 是类方法的第一个参数，表示类本身。在类方法中，你可以通过 `cls` 来访问或修改类属性，但定义类属性时不需要使用 `cls`。
3. **实例访问类属性**：实例可以访问类属性，但如果实例修改类属性，会在实例中创建一个新的实例属性，而不会改变类本身的属性。

希望这个解释清晰明了！如果还有任何问题，欢迎继续提问。



## python中的`*` 解包

在 Python 中，`*` 解包符号用于将可迭代对象（如列表、元组等）中的元素解包并传递给函数、方法或构造器。具体来说，`*` 可以在函数调用时将一个可迭代对象中的元素作为独立的参数传递，也可以在函数定义时收集位置参数。

用法示例

1. **函数参数解包**

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # 等价于 add(1, 2, 3)
print(result)  # 输出 6
```

在这个例子中，`*numbers` 将列表中的元素解包并作为独立的参数传递给 `add()` 函数。

1. **在列表或字典解包时使用 `\*`**

```python
# 使用 * 解包列表
list1 = [1, 2, 3]
list2 = [4, 5]
combined = [*list1, *list2]
print(combined)  # 输出 [1, 2, 3, 4, 5]

# 使用 ** 解包字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined_dict = {**dict1, **dict2}
print(combined_dict)  # 输出 {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

1. **在函数参数中收集多个参数**

```python
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3, 4)  # 输出 1 2 3 4
```

在这个例子中，`*args` 会将传入的多个参数收集到一个元组中。

在 `@data(*read_num_json())` 中的使用

在你的代码中，`@data(*read_num_json())` 使用 `*` 将 `read_num_json()` 返回的列表中的每个元素解包并传递给 `@data` 装饰器。假设 `read_num_json()` 返回的数据是 `["666", "777", "888"]`，`@data(*read_num_json())` 相当于将这些值传递给 `@data('666', '777', '888')`。

**返回内容**：

```python
return json.load(open('num.json', 'r', encoding='utf-8'))
```

假设 `num.json` 文件内容是 `["666", "777", "888"]`，那么 `json.load(open('num.json', 'r', encoding='utf-8'))` 将返回一个列表 `["666", "777", "888"]`，该列表会被解包传递给 `@data`。

**解包解释**： 不需要额外的解包操作，因为 `@data` 装饰器本身已经负责处理数据的传递。`*` 用于将列表中的每个元素作为独立参数传递给装饰器。



## python中的`*`和`**`

在 Python 中，`*` 和 `**` 有不同的用法和意义，具体如下：

1. 单星号 `*`

1.1 在函数参数中
 `*` 表示可变长度的 **位置参数**，它允许函数接受任意数量的位置参数，并将它们存储为一个元组。

```python
def example_function(*args):
    print(args)

example_function(1, 2, 3)  # 输出：(1, 2, 3)
example_function('a', 'b')  # 输出：('a', 'b')
```

`*args` 是一个常见的写法，其中 `args` 是约定俗成的名字，实际可以用其他名字替代。接收的参数会以元组的形式存储在 `args` 中。

1.2 在函数调用中
 `*` 可以用于解包可迭代对象（如列表、元组等）为独立的参数传递给函数。

```python
def example_function(a, b, c):
    print(a, b, c)

values = [1, 2, 3]
example_function(*values)  # 输出：1 2 3
```

这里，`*values` 将列表 `[1, 2, 3]` 解包为单独的参数 `1, 2, 3`。

1.3 在列表/元组解包中
 `*` 可以在赋值操作中捕获多余的元素。

```python
a, *b, c = [1, 2, 3, 4]
print(a)  # 输出：1
print(b)  # 输出：[2, 3]
print(c)  # 输出：4
```

这里，`*b` 捕获了中间的元素。

1. 双星号 `**`

2.1 在函数参数中
 `**` 表示可变长度的 **关键字参数**，它允许函数接受任意数量的键值对参数，并将它们存储为一个字典。

```python
def example_function(**kwargs):
    print(kwargs)

example_function(a=1, b=2, c=3)  # 输出：{'a': 1, 'b': 2, 'c': 3}
```

`**kwargs` 是常见写法，其中 `kwargs` 是约定俗成的名字，实际可以用其他名字替代。接收的参数会以字典的形式存储在 `kwargs` 中。

2.2 在函数调用中
 `**` 可以用于解包字典为关键字参数传递给函数。

```python
def example_function(a, b, c):
    print(a, b, c)

values = {'a': 1, 'b': 2, 'c': 3}
example_function(**values)  # 输出：1 2 3
```

这里，`**values` 将字典 `{'a': 1, 'b': 2, 'c': 3}` 解包为关键字参数 `a=1, b=2, c=3`。

1. - 和 ** 的联合使用

在函数定义中，`*args` 和 `**kwargs` 可以一起使用，接受任意数量的位置参数和关键字参数。

```python
def example_function(*args, **kwargs):
    print('位置参数:', args)
    print('关键字参数:', kwargs)

example_function(1, 2, 3, a=4, b=5)  
# 输出：
# 位置参数: (1, 2, 3)
# 关键字参数: {'a': 4, 'b': 5}
```

`*args` 捕获所有的位置参数，`**kwargs` 捕获所有的关键字参数。

1. 总结

单星号 `*`：

- 用于定义可变长度的位置参数。
- 用于解包可迭代对象为单独的参数。
- 用于捕获多余的列表或元组元素。

双星号 `**`：

- 用于定义可变长度的关键字参数。
- 用于解包字典为关键字参数。

这两者是 Python 中非常灵活和强大的特性，常用于动态传参、数据解包和处理复杂函数调用的场景。



## ord和chr

**1. `ord()`**

- **作用**: 将单个字符转换为对应的 Unicode 码点（整数值）。

- **语法**: `ord(char)`

- **输入**: 一个字符（长度为 1）。

- **输出**: 字符的 Unicode 码点（整数）。

- 示例:

  ```python
  print(ord('A'))  # 输出: 65
  print(ord('😊')) # 输出: 128522
  ```

**2. `chr()`**

- **作用**: 将整数（Unicode 码点）转换为对应的字符。

- **语法**: `chr(i)`

- **输入**: 一个整数，范围在 `0` 到 `1114111`。

- **输出**: 与该整数对应的字符。

- 示例:

  ```python
  print(chr(65))     # 输出: 'A'
  print(chr(128522)) # 输出: '😊'
  ```

------

**`ord()` 和 `chr()` 的常见用途**

1. **字符和数字的互相转换**:

   ```python
   char = 'A'
   num = ord(char)
   print(num)           # 输出: 65
   print(chr(num))      # 输出: 'A'
   ```

2. **生成字符序列**:

   ```python
   chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
   print(chars)  # 输出: ['a', 'b', ..., 'z']
   ```

3. **计算字符之间的差值**:

   ```python
   print(ord('b') - ord('a'))  # 输出: 1
   ```

4. **处理 Unicode 字符**:

   ```python
   print(ord('你'))  # 输出: 20320
   print(chr(20320)) # 输出: '你'
   ```

------

**总结**

- **`ord()`**: 从字符到整数。
- **`chr()`**: 从整数到字符。
- 两者互为逆操作，可用于字符处理和编码任务。



## python中的sort

`list.sort()` 是 Python 列表的原地排序方法，常用的语法是：

```python
list.sort(key=函数, reverse=布尔值)
```

- **`key`**：指定一个函数，用于生成每个元素的排序依据。
- **`reverse`**：如果为 `True`，结果将按降序排序，默认值为 `False` 升序。

也可以不指定

```
list.sort()
```



## python中的匿名函数lambda

语法

```
lambda 参数: 函数体（将结果返回）
```

```
lambda x: x[0]  返回x数组的第一个元素
```

```python
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x: x[0])
```

