#现在来建立一个静态页的服务器  终于第一个有用的东西要出来了  哦哦 当然是假有用
from socket import*
from multiprocessing import Process
import re
#先建立套节字
sever = socket(AF_INET,SOCK_STREAM)
#sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sever.bind(('',8888))
sever.listen()
#设置静态文件根目录
HTML_ROOT_DIR = "./html"
def fun(cli,addr):
	while True:
		#获取请求数据
		
		date = cli.recv(1024)
		#j将获取数据按照行分割
		date_list = date.splitlines()
		#获取第一行信息
		start_line = date_list[0]
		#解析报文数据 	GET / HTTP/1.1 /到H之间为请求内容的目录
		file_name = re.match(r"\w+ +(/[^ ]*) ", start_line.decode("utf-8")).group(1)
		if "/"==file_name:
			file_name="/index.html"
		#打开文件获取数据
		file_f = open(HTML_ROOT_DIR+file_name,"rb")
		file_date = file_f.read()
		file_f.close()
		#构造响应数据
	
		response_start =  "HTTP/1.1 200 OK\r\n"
		response_header = "SEVER:FOXYI\r\n"
		response_body = file_date.decode("utf-8")
		responce = response_start+response_header+"\r\n"+response_body
		print(date)
		if date:
			#发送响应数据
			cli_so.send(bytes(responce,"utf-8"))
			cli_so.close()
			break
		else:
			cli_so.close	
			break

			
while True:
	cli_so,addr = sever.accept()
	print("用户[%s,%s]已链接"%addr)
	t = Process(target=fun(cli_so,addr))
	t.start()
#	cli_so.close()
