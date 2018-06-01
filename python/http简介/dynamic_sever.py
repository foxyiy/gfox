#接下来来一个动态的服务器代码 #写一半太累睡觉了 后面没难度 写不写看心情吧
"""动态服务器 """
from socket import*
from multiprocessing import Process
import re
#设置静态文件根目录
HTML_ROOT_DIR = "./html"
			
class Web_sever(object):
	#对该服务器进行初始化
	def __init__(self):
			
		#先建立套节字
		self.sever = socket(AF_INET,SOCK_STREAM)
		#sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sever.bind(('',8988))
		self.sever.listen()
	def start(self):	
		while True:
			cli_so,addr = self.sever.accept()
			print("用户[%s,%s]已链接"%addr)
			#用到一个fun函数当然是去定义一个了
			t = Process(target=self.fun(cli_so,addr))
			t.start()
			cli_so.close()
	def start_response(self,status,headers):
		
		#将得到的信息打包成响应头
		#令self.header = 打包好的信息头 
			
	def fun(self,cli_so,addr):
		while True:
			#获取请求数据
			
			date = cli_so.recv(1024)
			#j将获取数据按照行分割
			date_list = date.splitlines()
			#获取第一行信息
			start_line = date_list[0]
			#解析报文数据 	GET / HTTP/1.1 /到H之间为请求内容的目录
			file_name = re.match(r"\w+ +(/[^ ]*) ", start_line.decode("utf-8")).group(1)
			#此时拿到了件名称和路径 需要提取文件名称 /ctime.py
			if file_name.endwith(".py"):
				#导入该文件
				
				file_name = file_name[1:-3]
				m = __import__(file_name)
				env = {}
				#参数start_response需要定义
				m.applycation(env,self.start_response)			
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
				print(responce)
				cli_so.close()
			else:
				cli_so.close	
				break
	#已经有套节字了下来当然是接收内容并进行处理了
"""	def start(self):	
		while True:
			cli_so,addr = self.sever.accept()
			print("用户[%s,%s]已链接"%addr)
			#用到一个fun函数当然是去定义一个了
			t = Process(target=fun(cli_so,addr))
			t.start()
			cli_so.close()"""
def main():
#目的是建一个服务器 对客户端requset进行理
	web_sever = Web_sever()
	web_sever.start()

if __name__ == "__main__":
	main()
