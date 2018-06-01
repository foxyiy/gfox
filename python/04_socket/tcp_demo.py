#服务器的编写
from socket import*
from threading import Thread
#创建套节字 用于链接
tcp_sever_socket = socket(AF_INET,SOCK_STREAM)
#绑定地址
tcp_sever_socket.bind(('',8879))
#设定为被动监听模式
tcp_sever_socket.listen(11)
#得到客户端的套节字，等待客户端链接  用于传输数据的套节字
def recvdate(socket,address):
	while True:
		recvdate=client_socket.recv(1024)
		if len(recvdate)>0:
			print(str(recvdate.decode("gb2312")))
			print("")
		else:
			break
		send_date = "hello" 
		client_socket.send(send_date.encode("gb2312"))
while True:
	client_socket,clieninfo=tcp_sever_socket.accept()
#接收 发送数据
	thread = Thread(target=recvdate,args=(client_socket,clieninfo))
	thread.start()
tcp_sever_socket.close()
