import urllib
import requests
import urllib.request 
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
#url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
key = input("请输入单词：")
fromdata = {
"client":"fanyideskweb",
"action":"FY_BY_CLICKBUTTION",
"doctype":"json",
"from":"AUTO",
"salt": "1534217261640",
"i":key,
#"sign":"ce0fe6bd4f060135e5c0f69dd1b92f39",
"keyfrom":"fanyi.web",
"smartresult":"dict",
"to":"AUTO",
"typoResult":"false",
"version":"2.1"
        }
data = urllib.parse.urlencode(fromdata).encode("utf8")
headers = {
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Language" :"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Connection": "keep-alive",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Host": "fanyi.youdao.com",
"Origin": "http://fanyi.youdao.com",
"Referer": "http://fanyi.youdao.com/",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339$",
"X-Requested-With": "XMLHttpRequest",
#"Cookie": "OUTFOX_SEARCH_USER_ID=942907458@10.168.8.63; JSESSIONID=aaaNNXMhcWvO05f71Zmqw; OUTFOX_SEARCH_USER_ID_NCOO=175745102.5234947; ___rl__test__cookies=1529229040340"
}
response = requests.post(url,data=fromdata)
#request = urllib.request.Request(url,data=data,headers=headers)
#response = urllib.request.urlopen(request)
print(response.text)
