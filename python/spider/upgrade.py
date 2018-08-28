#调用该模块返回一个或多个可用的代理

#1.爬取所有代理并保存到本地 upgrade_ip
#2.从本地文件中测试选出可用代理，保存在数组中

import requests
import telnetlib
import threading
import  queue
from multiprocessing import Process
from lxml import etree

q = queue.Queue()

def sava_proxy(url):
   headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
   response = requests.get(url,headers = headers)
   html = response.text
   x_html = etree.HTML(html)
   ip_info = x_html.xpath("//tr[@class]") 
   
   with open("ip.txt",'a') as f:
       for i in ip_info:
           ip = i.xpath("./td[2]")[0].text
           port = i.xpath("./td[3]")[0].text
           ip_port = ip+":"+port     
           f.write(ip_port+"\n")

#将文件中的Ip存放在queue中
def get_proxy():
    with open("ip.txt")as f:
        while True:
            str = f.readline()  
            if not str:
                break
            q.put(str)

#验证代理是否有效
def get_test_proxy():
    while not q.empty():
        ip = q.get().split(":")[0].strip()
        port = q.get().split(":")[1].strip()
        if test_proxy(ip,port):
            return ip,port
        else:
            pass

def threas(fun):
    for i in range(30):
        t = threading.Thread(target = fun )
        t.start()
        t.join()

def test_proxy(ip,port):
    try:
         telnetlib.Telnet(ip,port=port,timeout=3)
    except:
        print("field   "+ip+":"+port)
        return False
    else:
        print("success   "+ip+":"+port)
        return True  


if __name__ == '__main__':
    url = "http://www.xicidaili.com/nt/"
    sava_proxy(url)
    get_proxy()
    threas(get_test_proxy)
