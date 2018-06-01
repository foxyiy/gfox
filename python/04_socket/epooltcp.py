#一个epool版服务器 单线程达到处理多任务的目的
from socket import *
import select

#1.创建套节字 
sever = socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定
sever.bind('',7878)
#监听
sever.listen(10)

#创建epool对象
epoll = select.epoll()
#将创建的套节字添加到 epool的事件监听中
#fino方法返回文件描述符
#select.EPOOLINn表示只检测可读事件 	EPOLLET表示边沿触发
pool.register(sever.fino(),select.EPOOLIN|select.EPOOLLET)

connections = {}
addresses = {}

while True:
	#得到收到消息的所有套节字
	epoll_list = epoll.pool()
#对得到的套节字进行处理
for fd,events in epoll_list
	#fd 为监听到的套节字的文件描述符
	#当监听到服务器套节字消息时进行的处理
	if fd == sever.fileno():
		coon,addr = sever.accept()
		#将该套节字的信息以键值对的方式储存在字典中	
		connections[coon.fileno]=coon
		addresses[coon.fileno]=addr
		#注册客户端套节字
		epoll.register(coon.fileno,select.EPOOLIN|select.EPOOLLET)
	elif events == select.SELECT.EPOLLIN:
		#此时有消息的套节字为客户端可以接收消息套节字
		recvdate = connections[fd].recv(1024)
		#对接收到的数据进行处理
		if recvdate:
			print(recvdate)
		else:
			epoll.unregister(fd)
			connections[fd].close()

