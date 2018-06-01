#创建多线程
from threading import Thread
#通过thread创建多线程
def demo ():
	print("test")
thread = Thread(target=demo)
thread.start()
#当然也可以创建子类覆盖run方法通过实例对象创建多线程
class Demo(Thread):
	def run(self):
		print("run")
d=Demo()
d.start()	

