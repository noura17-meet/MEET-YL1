class Animal(object):
	def __init__(self,sound,name,age):
		self.sound= sound
		self.name= name
		self.age=age
	def eat(self,food):
		print(self.name + "is eating" + food)

	def sleep(self,dream): 
		print("the " + str(self.age) + " years old " + self.name + "is dreaming about" + dream)
	
		 
class dog(Animal):
	def bark(self,function):
		print("the " + "dog" + function)
	
	

class bird(Animal):
	def fly(self,function):
		print("the " + "bird" + function)
class chicken(bird):
	print("chicken doesn't fly")
	
class fish(Animal):
	def swim(self,function):
		print("the " + "fish" + function)

	
	

