class Itcast(object):
	def __init__ (self,subject1):
		self.subject1=subject1
		self.sub2="sub2"
	def __getattribute__(self,sub):#属性访问拦截器 用于对访问属性时的判断和操作 如log日志
		if sub=="subject1":
			return "禁止访问"
		else:
			return object.__getattribute__(self,sub)
	def show(self):
		print("show")
it=Itcast("sub")
print(it.subject1)
print(it.sub2)	
it.show()#先把show 当作一个属性传给 getattritube 得到一个返回值
#然后执行返回值（）即 方法（）
#返回时不能返回一个方法 否则引起循环调用造成 bug
