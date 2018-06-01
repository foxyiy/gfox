from socket import *
udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(('',8888))
while True:
	recv=udp_socket.recvfrom(8080)
	print(str(recv[0].decode("gb2312")))