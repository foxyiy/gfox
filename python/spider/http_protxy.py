import requests
import telnetlib
from lxml import etree
xi_ci_url = "http://www.xicidaili.com/nt/"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
response = requests.get(xi_ci_url,headers = headers)
html = response.text
x_html = etree.HTML(html)
ip_info = x_html.xpath("//tr[@class]")

print(len(ip_info))

with open("ip.txt",'w') as f:
        
    for i in ip_info:
        ip = i.xpath("./td[2]")[0].text
        port = i.xpath("./td[3]")[0].text
        ip_port ="{"+"\"ip_port\""+":\""+ip+":"+port+"\", "+"\"user_passwd \": "+"\"\""+"}"
        try:
             telnetlib.Telnet(ip,port=port,timeout=5)
             
        except:
            print("field")
        else:
            print("success")
            f.write(ip_port+"\n")

