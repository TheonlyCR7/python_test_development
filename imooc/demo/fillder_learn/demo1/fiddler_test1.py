#coding=utf-8
import requests
import json
#上传文件
url = 'https://www.imooc.com/user/postpic'

# file = {
#     "fileField":("文件名称",open("路径","rb"),"image/jpg"),
#     "type":"1"
# }
file = {
    "fileField":("Snipaste_2024-06-19_19-47-41.jpg",open("D:/Document/Snipaste_2024-06-19_19-47-41.jpg","rb"),"image/jpg"),
    "type":"3"
}
cookie = {
    "apsid":"llMjQ5ZDg3OTNkODExNjJmNjBkNWE4Mzk4Mzg1MGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzI4MjExNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAyMzExMTI5MDQ5M0BxcS5jb20AAAAAAAAAAAAAAAAAADQ4Y2VjYzZkMzAzOTM3MDhiMDVjNmU0MmQ1MzljZGM4qwFxZ%2BqWHGM%3DZD"
}

res = requests.post(url, files=file, cookies=cookie, verify=False).text
print(res)
# with open("mukewang.apk","wb") as f:
#     f.write(res.content)
#res = requests.post(url,files=file,cookies=cookie,verify=False).json()
# print(res)
# #res = requests.post(url,files=file,cookies=cookie,verify=False).json()
# print(res)
