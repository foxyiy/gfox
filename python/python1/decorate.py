#当程序碰到装饰器时会执行对函数进行装饰，当调用函数时返回装饰后的结果
#当对函数进行多次装饰时 在外部及返回时的装饰是从下往上  在内部函数中的装饰从上往下   装饰顺序：外部函数，内部函数   返回值
def d1(f):
	print("外部装饰1")
	def inner(*args,**kwargs):#参数通用 
		print("内部装饰1")
		ret=f(*args,**kwargs)
		return ret#对有返回值的函数进行处理  无返回值的则返回空  返回值通用
	return inner
def d2(f):
	print("外部装饰2")
	def inner():
		print("内部装饰2")
		f()
	return inner
@d1#当装饰器带参数时表示 装饰器外部还有一个函数 先执行外部函数 再对函数进行装饰  能够起到在运行时有不同#的功能
@d2#f=d1(f) 此时指向装饰函数内部函数的引用
def f(a,b):
	print("yuan_han_shu")
f(a,b)#调用装饰器内部函数所以在 内部函数加参数
