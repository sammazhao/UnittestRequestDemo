import requests
import chunk
from requests.cookies import RequestsCookieJar
import urllib3
import json
urllib3.disable_warnings()
url=u'https://vmaosupdb2.gencos.com/APXLogin/api/authenticate'
# r=requests.get(url)
getPayload={'loginname':'admin', 'password':'advs'}
r=requests.get(url, getPayload, verify=False)
print("url is", r.url)
print("json is: ", r.json)
print(r.status_code)
print(r.encoding)
print("Cookie is: ", r.cookies)
print("headers is: ", r.headers)
r.encoding='unicode'

headers={'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
'Connection': 'keep-alive',
'Cookie': 'AOAuth1=SessionCode=2F9C444F-5C5E-4085-A254-F7C3C6E13E47; AODBID1=DatabaseIdentifierCode=VgBNAEEATwBTAFUAUABEAEIAMgBcAFMAUQBMAF8ATABBAFQASQBOADEAXwAyADAAMQA2AC4AQQBQAFgARgBpAHIAbQAEQ',
'Host': 'vmaosupdb2.gencos.com',
'Referer': 'https://vmaosupdb2.gencos.com/APXUILogin/',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site':'same-origin' ,
'SessionCode': '2F9C444F-5C5E-4085-A254-F7C3C6E13E47',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

# demo:  将cookies添加到requests session对象中
# 创建cookiejar实例
cookie_jar=RequestsCookieJar()

#将获取的cookie转换为字典
cookie_dict=requests.utils.dict_from_cookiejar(r.cookies)

#将字典转为CookieJar：
cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)

#创建session，添加cookies
# 往下使用requests的地方，直接使用session即可，session就会保存服务器发送过来的cookie信息
session=requests.session()
session.cookies=cookies

url2=u'https://vmaosupdb2.gencos.com/APXLogin/api/internal/InterestedParty/search?$d=y&$m=n&$s=40&$c=-226021101' 

jsonheaders = {'Content-Type': 'application/json'}
payload2=json.dumps({
        "Search": {
            "Query": {
                "Joins": [],
                "CriteriaList": [],
                "Entity": "InterestedParty"
            },
            "Options": {
                "PageNumber": 0,
                "PageSize": 50,
                "OrderBy": [
                    "ContactName asc",
                    "ReportHeading asc"
                ],
                "UseDistinct": False
            }
        }
})

#辅助方法：调整response显示样式
# json.dumps()用于将字典形式的数据转化为字符串，json.loads()用于将字符串形式的数据转化为字典
def betterPrint(json_str):
    return json.dumps(json.loads(json_str), indent=4)


r2=session.post(url=url2, headers=jsonheaders, data=payload2, verify=False)
rr=betterPrint(r2.text)

r2.raise_for_status()

# 将响应内容以text形式写入文件中
with open('filename', 'w') as fd:
    fd.write(rr)

