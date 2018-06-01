from socket import *

csocket = socket(AF_INET,SOCK_STREAM)
address = ("10.145.167.233",8879)
csocket.connect(address)
while True:
	send_date = input("输入：")
	csocket.send(send_date.encode("gb2312"))
	recvdate = csocket.recv(1024).decode("gb2312")
	print("")
	print(recvdate)
csocket.close()

