import types
def eat(self):
	print(self)
	print("eat")
class Person(object):
	"""docstring for Person"""
	def __init__(self,name):
		super(Person, self).__init__()
		self.name=name
p=Person(100000)
p.sum=100	
p.eat= types.MethodType(eat,p)
p.eat()
print(dir(p))

		
