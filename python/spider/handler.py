#用代理处理器获取数据步骤
#1.创建代理处理器对象或私密代理器对象 
#2. 创建opener对象 
#3. 构造请求头部信息
#4. 构造请求体request
#5. opener.open(request)发送请求体
import ssl
#代理的简单使用
import urllib.request
#创建处理器对象
proxy_handler = urllib.request.ProxyHandler({"http" : "93.183.149.245:53281"})
#处理https请求 
ssl._create_default_https_context = ssl._create_unverified_context  
#创建私密代理处理器对象
#http_handler = urllib.request.ProxyHandler({"http":"user:passwd@ 107.21.56.41:80"})
#创建opener对象
opener = urllib.request.build_opener(proxy_handler)
url = "http://www.daanjia.com/plugin.php?id=nimba_newlogin&uid=484904/"
headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",

#        "Cookie":"BAIDUID=2A774322C66F9F34BED78199EEDCF0EF:FG=1; BIDUPSID=2A774322C66F9F34BED78199EEDCF0EF; PSTM=1528174156; BD_UPN=123353; BDUSS=TJHbmltRXVhNkFqd1JmTC1lZzVQUWZXbDhjMlBSaXU2Y0tlY21oeUs2dG13VUJiQVFBQUFBJCQAAAAAAAAAAAEAAABiWgSjvsnDztLgyLvUuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGY0GVtmNBlbU; cflag=5%3A3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; H_PS_PSSID=1458_21103_26350_22160; sugstore=0",
       "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"        }
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
#print(response.read().decode("utf8"))
print(response.read())
