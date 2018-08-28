import urllib.request
import urllib
wd = input("请输入查询关键字:")
w = {"wd":wd}
wd = urllib.parse.urlencode(w)
url = "http://www.baidu.com/s?"+wd
request = urllib.request.Request(url)
resoponse = urllib.request.urlopen(request)
file = resoponse.read().decode("utf8")
serch = open("./serch.html",'w')
serch.write(file)
serch.close()
