from socket import *
#创建udp套节字
udp_s = socket(AF_INET,SOCK_DGRAM)
#通过udp 发送数据
udp_s.sendto(b"hello word",("192.168.119.115",8080))
#太累了 对于端口的绑定 发送数据 编码等问题明天再去解决 现在去happy happy bye#...

#hello 我又回来了 开始谈谈绑定和编码问题

#给一个套节字绑定固定的 ip and 端口
udp_s.bind((('',8888))
#表示绑定本机 ip 和 8888端口 哎 没有一个可以实验的好心
#udp_s.recvfrom(1024)
#接收1024个字节的数据 返回 内容 发送方的 ip 和端口
#解决编码问题：
#python3 默认接收字节类型对象 
#send_date=input()#发送的数据 
#usb_s.sendto(send_date.encode("utf-8"))#字符串的encode方法将输入变为要转成的字#符形式使接收方可以正确解码
#当接收到数据时： 先从返回值中挑出字符串再通过字符串的decode()方法解码
#encode()完成编码 decode方法完成解码
#好了该做些有用的东西了
