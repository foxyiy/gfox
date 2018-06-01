#生成器的第一种创建方式
# b=(x*3 for x in range(10))
#斐波那器数列
def ger():
	a,b=0,1
	for i in range(10):
	       temp=yield b#当执行到该句时会返回b的值然后停止执行等待下个next调##用生成器的另一种创建方式
#并不会把b的值返回给 temp而是直接返回给 next 即temp 得到的值为空
		a,b=b,a+b
c=ger()#创建生成器

#以下两种操作方式是相同的
#next(a)
#a.__next__()
#a.send("hhhh")可以给temp赋值 并且得到你生成的结果
#第一次不能赋值可写为a,send(None)
#yield 的另一种用途是 协程 达到多任务的实现
