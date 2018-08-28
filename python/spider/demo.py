import urllib.request
ur_headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "Cookie":"BAIDUID=2A774322C66F9F34BED78199EEDCF0EF:FG=1; BIDUPSID=2A774322C66F9F34BED78199EEDCF0EF; PSTM=1528174156; BD_UPN=123353; BDUSS=TJHbmltRXVhNkFqd1JmTC1lZzVQUWZXbDhjMlBSaXU2Y0tlY21oeUs2dG13VUJiQVFBQUFBJCQAAAAAAAAAAAEAAABiWgSjvsnDztLgyLvUuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGY0GVtmNBlbU; cflag=5%3A3; BD_HOME=1; H_PS_PSSID=1458_21103_26350_22160; sugstore=0",
       "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"

        }

url = "http://www.baidu.com/"
request = urllib.request.Request(url,headers = ur_headers)
response = urllib.request.urlopen(request)
print (response.read().decode('utf8'))
#print( response.info)
