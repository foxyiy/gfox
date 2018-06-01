import os
import time

def demo():
	num=1
	ret = os.fork()
	if ret==0:#主进程大于0 子进程等于0 当执行到fork时会创建子进程
		while True:
			time.sleep(1)
			print("-------1-------")
			num+=1
			print(num)
	else:
		while True:
			print("-------2-------")
			time.sleep(3)
			print(ret)
			print(num)
demo()
#os.getipd() getippd() 获取进程ipd 父进程ipd
#全局变量对于各进程是独立的 一个修改不会影响另一个
