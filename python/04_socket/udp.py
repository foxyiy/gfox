from socket import*
#udp 的广播
dest=('<broadcast>',7770)#<broadcast>表示本地广播段   即xxx.xxx.xxx.255 
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)#表示可以用于广播
s.sendto(b'hello word',dest)
#
