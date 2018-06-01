import os
from socket import*
def sock():
	csocket = socket(AF_INET,SOCK_STREAM)
	address = ("10.146.93.190",6879)
	csocket.connect(address)
	csocket.send("hhh".encode("gb2312"))
	ret = os.fork()
	if ret==0:
		for x in range (7):
			sock()
			print("kkk")
sock()
