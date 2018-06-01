import gevent
import time 
import sys
from gevent import socket,monkey
monkey.patch_all()
#gevent 用于io密集型 
#gevent对常用耗时操作进行了重写 当遇到耗时操作时就会切换操作
def sever():
	s = socket.socket()
	s.bind(('',7789))
	s.listen(5)
	while True:
		clin,addr = s.accept()
		gevent.spawn(clinn,clin)
def clinn(clin):
	while True:
		date = clin.recv(1024)
		if date:
			print(date)
		else:
			clin.close()
			break
sever()

