import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = 'https://coding.m.imooc.com/api/classindex/recommendList?cid=445'

# data = {
#     'Code':'738955',
#     'TrustThisDevice':'true',
#     'Type':'Phone',
#     'IsRemember':'False',
#     'ReturnUrl':'https://www.cnblogs.com/',
#     '_RequestVerificationToken':'CfDJ8DfB03_iObVLoqH7ndAeeDgQhdm2jbyXhtsIjeXBkPOC9rbD6tJgMV_KLBOKGxqVwko8TY8AdhkWj61o7HWRko_a5ESw2lAD08L1chCYmD_sGgrfK2qCh5Rbhn-dfL09fr9r9MsNxgU1Sfsqq_K7QTo',
# }
data = {
    'cid':'445'
}
# cookie = "07CA2D821208A2F4C4FEEFB5E582AE63D31DCB4931C7CD90F570DDF2F8FEEA2CD534ED3D18F9BE5981320B556C40D1BC681F9C1B6B8F5EEDEB5A88F18B28D26D97A4D51F99A87D55D7A582FC5336F61F62777C4B"
# res_text = requests.get(get_url,verify=False).text
# print(res_text)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# res = requests.post(url, data, verify=False)
# print(res.status_code)  # 打印响应状态码
# print(res.text)         # 打印响应内容
#
# json_res = res.json()
# print(json.dumps(json_res,indent=4,ensure_ascii=False))
res = requests.get(url, verify=False)
print(res.status_code)  # 打印响应状态码
print(res.text)         # 打印响应内容
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
res_json = res.json()
res_json = json.dumps(res_json, indent=4, ensure_ascii=False)
print(res_json)
