class Test(object):
	"""docstring for Test"""
	def __init__(self):
		self.__num=100#属性私有化
	@property#通过装饰器使用 property 方法
def num(self):
		return self._num
	@num.setter
	def num(self,num):
		self._num =num 
	#num=property(set_num,get_num)#对外提供方便的访问方法
	#通过对属性的私有化并对外提供访问方法可以保证外部合理访问对象属性	
t=Test()
t.num=200
print(t.num)
"""同名变量子类会覆盖父类
_xxx  不能用 from moudule import* 导入
和对象子类可以访问 可以只导入一个模块"""
