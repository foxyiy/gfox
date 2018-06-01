from multiprocessing import Process
import time

def demo():
	print("----1-----")

p=Process(target=demo)#创建进程 并指向要运行的代码
p.start()
p.join()#阻塞方法 等待 调用的进程执行结束或者固定的时间才执行下一句
print("main")
#process 创建的进程 主进程不结束 子进程不会结束
#p.terminate() 立即终止该进程

class NewProcess(Process):
	def pa(self):
		print("-----1-----")

	def pb(self):
		print("-----2-----")
	
	def run(self):
		pa()
		pb()
p=NewProcess()
p.start()
