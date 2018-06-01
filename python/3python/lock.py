from threading import Thread,Lock
import time
#互斥锁的写法
"""
lock = Lock()
num = 0
def demo1():
	global num
	for x in range(1000000):
		lock.acquire()
		num=num+1
		lock.release()
	print(num)
def demo2():
	global num
	for x in range(1000000):
		lock.acquire()
		num=num+1
		lock.release()
	print(num)
thread1 = Thread(target=demo1)
thread2 = Thread(target=demo2)
thread1.start()
thread2.start()
"""
#死锁的产生与解法
#死锁产生的原因大多是因为多个函数多个锁的相互调用所以先定义两个函数
#如下就产生了死锁 解决死锁的一种办法是i添加超时时间等待

def demo1():
	l1.acquire()
	print("----1----")
	time.sleep(1)
	while true:
		if l2.acquire(2):
			l2.release()
			print("test")
		l1.release()
		print("demo")
		if l2.acquire():
		l2.release()
l1.release()
def demo2():
	l2.acquire()
	print("----2---")
	time.sleep(1)
	if l1.acquire(2):
		l1.release()
	l2.release()
l1 = Lock()
l2 = lock()
t1=thread(target=demo1)
t2=Thread(target=demo2) 
t1.start()
t2.start()
#额额  貌似这个解决并不咋的。需要修改下 算了算了 记下同步与异步去看网络那部分了
#同步 ：同步是锁的协约 等待
#异步：回调函数实现异步  callback 例如 pool.apply_async(fun=..,callback='')
#      当子进程执行宛 fun指向的函数时 子进程结束 父进程不再执行他所执行的
#      去执行回调函数
#GIL锁 由于是伪多线程 所以效率较低 此时通过c语言写关键部分
	
#加一句拜拜 去看网络编程了 那将很有意思
