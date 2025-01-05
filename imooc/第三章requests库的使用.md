以下是系统梳理的 Python `requests` 库笔记，包含基本用法、进阶技巧及常见问题。你可以直接复制到你的笔记中。

------

## **Python `requests` 库系统梳理**

### **1. `requests` 库简介**

`requests` 是 Python 中最常用的 HTTP 请求库，用于与 Web 服务交互。它简单易用、功能强大，支持发送 HTTP/HTTPS 请求。

------

### **2. 安装**

```bash
pip install requests
```

------

### **3. 基本用法**

#### **3.1 GET 请求**

获取资源的常见操作。

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# 查看响应内容
print(response.text)  # 返回响应内容（字符串形式）
print(response.json())  # 解析为 JSON 格式
print(response.status_code)  # HTTP 状态码
```

#### **3.2 POST 请求**

提交数据到服务器。

```python
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())  # 返回 JSON 格式的响应内容
```

#### **3.3 其他请求类型**

支持多种 HTTP 方法：

- PUT: 更新资源
- DELETE: 删除资源
- PATCH: 局部更新资源

```python
# PUT 请求
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json={"title": "updated title"})

# DELETE 请求
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

# PATCH 请求
response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json={"title": "patched title"})
```

------

### **4. 请求参数**

#### **4.1 URL 参数**

GET 请求确实是通过 URL 向服务器发送参数的，而 `params` 是 `requests` 提供的一种方便传递 URL 参数的方式，它将参数自动拼接到 URL 中，从而提高代码的可读性和灵活性。

* 手动拼接 URL 参数可能会出错，例如忘记添加 `?` 或 `&`，而 `params` 会自动完成这些操作。
* 当参数数量较多或需要动态生成时，手动拼接 URL 不方便，使用 `params` 更加灵活。

通过 `params` 传递查询参数：

```python
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
response = requests.get(url, params=params)

print(response.url)  # 查看请求的完整 URL
print(response.json())
```

#### **4.2 Headers**

在请求中自定义头部信息：

```python
url = "https://jsonplaceholder.typicode.com/posts"
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get(url, headers=headers)

print(response.status_code)
```

#### **4.3 Cookies**

管理和发送 Cookies：

```python
# 发送带 Cookie 的请求
cookies = {"session_id": "123456"}
response = requests.get("https://example.com", cookies=cookies)

# 查看响应的 Cookie
print(response.cookies)
```

#### **4.4 文件上传**

通过 `files` 上传文件：

```python
url = "https://httpbin.org/post"
files = {"file": ("test.txt", open("test.txt", "rb"))} # 固定格式
response = requests.post(url, files=files)

print(response.json())
```

------

### **5. 响应处理**

#### **5.1 响应属性**

```python
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)  # HTTP 状态码
print(response.headers)  # 响应头部
print(response.text)  # 响应内容（字符串）
print(response.json())  # JSON 格式
print(response.content)  # 响应内容（字节流）
```

#### **5.2 状态码检查**

```python
if response.status_code == 200:
    print("请求成功")
else:
    print(f"请求失败，状态码：{response.status_code}")
```

------

### **6. 超时和重试**

#### **6.1 设置超时**

通过 `timeout` 设置请求超时时间：

```python
response = requests.get("https://example.com", timeout=5)
```

#### **6.2 重试机制**

使用 `requests.adapters` 提供的 `HTTPAdapter` 实现自动重试：

```python
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

response = session.get("https://example.com")
```

------

### **7. 认证**

#### **7.1 Basic Auth**

```python
from requests.auth import HTTPBasicAuth

url = "https://example.com"
response = requests.get(url, auth=HTTPBasicAuth("username", "password"))
```

#### **7.2 Token Auth**

```python
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get("https://example.com", headers=headers)
```

------

### **8. SSL 验证**

#### **8.1 跳过 SSL 验证**

```python
response = requests.get("https://example.com", verify=False)
```

#### **8.2 自定义证书**

```python
response = requests.get("https://example.com", verify="/path/to/certfile")
```

------

### **9. 会话管理**

使用 `Session` 对象保存连接、Cookie 和 Headers。

```python
session = requests.Session()
session.headers.update({"Authorization": "Bearer YOUR_TOKEN"})

# 使用同一个会话发送多次请求
response1 = session.get("https://example.com/api1")
response2 = session.get("https://example.com/api2")
```

------

### **10. 异常处理**

处理常见异常，如连接错误、超时等。

```python
import requests

try:
    response = requests.get("https://example.com", timeout=5)
    response.raise_for_status()  # 检查 HTTP 错误
except requests.Timeout:
    print("请求超时")
except requests.RequestException as e:
    print(f"请求失败：{e}")
```

------

### **11. 测试和调试技巧**

#### **11.1 打印请求细节**

```python
response = requests.get("https://example.com")
print(response.request.headers)
print(response.request.body)
```

#### **11.2 使用 Fiddler 或 Charles 代理**

设置 `proxies` 参数：

```python
proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888",
}
response = requests.get("https://example.com", proxies=proxies)
```

------

### **12. 常见问题**

1. **如何处理大文件下载？** 使用 `stream=True`：

   ```python
   response = requests.get("https://example.com/largefile", stream=True)
   with open("largefile.zip", "wb") as f:
       for chunk in response.iter_content(chunk_size=1024):
           f.write(chunk)
   ```

2. **如何查看完整请求 URL？**

   ```python
   print(response.url)
   ```

3. **如何发送复杂 JSON 数据？**

   ```python
   response = requests.post("https://example.com", json={"key": "value"})
   ```

------



## 模拟get请求

```python
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = 'https://coding.m.imooc.com/api/classindex/recommendList?cid=445'

res = requests.get(url, verify=False)
print(res.status_code)  # 打印响应状态码
print(res.text)         # 打印响应内容
```

运行结果

```
D:\software\Anaconda\envs\unittest\python.exe D:\myCode\Github\python_test_development\demo\unittest_learn\cnblog\star_test.py 
200
{"status":1,"data":[{"id":"73","type":4,"type_name":"体系课","name":"Java架构师-技术专家","short_description":"Java程序员进级架构师的核心技能图谱与最佳成长方案","pic":"https://img1.sycdn.imooc.com/climg/5fe40179080a441302160304.jpg","level":"","numbers":"2672","learn_rate":-1,"is_new":0,"is_hot":0,"renovate":0,"authorized":0,"price":"6600.00","pay_price":"3299.00","target_url":"http://class.imooc.com/sale/javaarchitect","teacher_name":"慕课网讲师团","teacher_desc":"","act_name":[{"name":"特惠价","end_time":0}]},{"id":74,"type":1,"type_name":"实战课","name":"Vue.js2.5+cube-ui重构饿了么App（经典再升级）","short_description":"掌握Vue1.0到2.0再到2.5最全版本应用与迭代，打造极致流畅的WebApp","pic":"//img1.sycdn.imooc.com/szimg/5fe43feb080b265b02160304.jpg","level":"进阶","numbers":9868,"learn_rate":-1,"is_new":0,"renovate":"1","authorized":0,"pay_price":"198","price":198,"target_url":"https://coding.imooc.com/class/74.html","teacher_name":"ustbhuangyi","teacher_desc":"前端架构师","act_name":[],"is_hot":0},{"id":203,"type":1,"type_name":"实战课","name":"Vue2.5-2.6-3.0开发去哪儿网App 零基础入门到实战","short_description":"课程紧跟Vue3版本迭代，企业主流版本Vue2+Vue3全掌握","pic":"//img1.sycdn.imooc.com/szimg/5fe43fef08d6427a02160304.jpg","level":"初阶","numbers":10675,"learn_rate":-1,"is_new":0,"renovate":"1","authorized":0,"pay_price":"89","price":266,"target_url":"https://coding.imooc.com/class/203.html","teacher_name":"Dell","teacher_desc":"资深前端工程师","act_name":[{"name":"特惠价","end_time":"1993478399"}],"is_hot":0},{"id":320,"type":1,"type_name":"实战课","name":"Node.js 从零开发 web server博客项目","short_description":"从入门到实战，一站式掌握 Node.js+Express+Koa2","pic":"//img1.sycdn.imooc.com/szimg/63328f5509ce2cc802160304.jpg","level":"初阶","numbers":4051,"learn_rate":-1,"is_new":0,"renovate":"1","authorized":0,"pay_price":"338","price":338,"target_url":"https://coding.imooc.com/class/320.html","teacher_name":"双越","teacher_desc":"资深前端工程师","act_name":[],"is_hot":0}],"errorCode":1000,"errorDesc":"成功","timestamp":1735540728197}

进程已结束，退出代码为 0
```



处理json数据

上面直接输出的返回值数据看起来杂乱，没有格式化

```
res_json = res.json()
# indent为缩进，ensure_ascii=False表明不转义非ASCII字符
res_json = json.dumps(res_json, indent=4, ensure_ascii=False)
print(res_json)
```

> ensure_ascii默认值为True，将非 ASCII 字符转义为 Unicode 转义序列。例如，`"汉字"` 会变成 `"\\u6c49\\u5b57"`。

再运行，结果类似为

![image-20241230144753112](C:\Users\Mrliu\AppData\Roaming\Typora\typora-user-images\image-20241230144753112.png)

tip:

很多情况下，返回值不是严格的json格式，直接转义会发生错误。

出现该情况时，要先用`.text`打印查看一下原始的内容



## 文件上传操作

见第一章



## 下载文件

下载文件时，想要获取对应的URL，可以查看网页调试，通过网络查看到真正的下载地址

![image-20241230152226257](C:\Users\Mrliu\AppData\Roaming\Typora\typora-user-images\image-20241230152226257.png)

代码

```python
#coding=utf-8
import requests
import json

download_url = 'http://file.mukewang.com/imoocweb/webroot/mobile/imooc7.2.010102001android.apk'

res = requests.get(download_url)
with open("mukewang.apk","wb") as f:
    f.write(res.content)
#res = requests.post(url,files=file,cookies=cookie,verify=False).json()
print(res)
#res = requests.post(url,files=file,cookies=cookie,verify=False).json()
print(res)

```

运行

```
<Response [200]>
<Response [200]>
```

![image-20241230153404788](C:\Users\Mrliu\AppData\Roaming\Typora\typora-user-images\image-20241230153404788.png)



## header

网站会对header进行校验，直接发送请求可能会被网站识别为非法请求，所以需要添加header

![image-20241230154148084](https://s2.loli.net/2024/12/30/rwZuOXvWAYnLp4C.png)

```
header = {
    'Host':'m.imooc.com',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':'https://m.imooc.com/',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'token':res1
}
```



## 加密的请求头header

![image-20241230154711751](https://s2.loli.net/2024/12/30/U34VyG72CbANRsT.png)



模拟加密一下

```
#coding=utf-8
import requests
import hashlib
import json
imooc = "imooc.com" # 基础值
md5 = hashlib.md5()

data = str({
    'user':'11111'
})
md5.update(data.encode('utf-8')) # 一定要转码
res1 = md5.hexdigest()
print(res1)
```

结果

```
c5616fd4f8687c30ee74030d6e9e0c2e
```

将加密值作为token，放入header中

