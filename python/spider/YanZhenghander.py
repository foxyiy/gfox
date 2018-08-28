from urllib import request
pwd = request.HTTPPasswordMgrWithDefaultRealm(None,url = 'http://www.baidu.com/',user = 'foxyi',pssswd='123456')
authHandler = request.HTTPBasicAuthHandler(pwd)
openner = request.build_opener(authHandler)
print("hello")
