from animalfile import *
import random
name=['jeff','jasmine','yara','hiba','ahmad','sara','anas','jane','caroline','ted']
age=[12,13,70,35,34,56,72,22,45,62]
for i in range(50):
	animal= Animal("woof",name[random.randint(0,9)],age[random.randint(0,9)])
	animal.eat("bamba")
	
jeff = dog()
jeff.bark()
fish.swim()
bird.fly()
chicken.fly()

#dog= Animal("woof","jeff",17)
#cat= Animal("meow","lolo",4)


#print(dog.sound)

#dog.eat("bamba")
#cat.eat("bamba")

#dog.sleep("food")
#cat.sleep("bed")


