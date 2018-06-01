from multiprocessing import Pool
import time
import os
def demo ():
	for x in range(10):
		print(x)

p=Pool(3)

for x in range(5):

	p.apply_async(demo)#p.appily(demo),阻塞式方法
	print("----%d----"%x)

p.close()#关闭进程池 不能在添加任务
p.join()#主进程结束后子进程会停止运行
print("---main----")

