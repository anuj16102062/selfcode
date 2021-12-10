class pat:
	def __init__ (self,name,age):
		self.name = name
		self.age = age
	def show(self):
		print(f"matru and {self.name} or cvbn {self.age}")
class cat(pat):
	def __init__(self ,name,age,color):
		self.color = color
		super().__init__(name,age)
	def speak(self):
		print('mauwww')
	def show1(self):
		print(f"matru hgdjhs {self.name} or cvbn {self.age} === {self.color}")
class dog(pat):
	def speak(self):
		print('bark')
p = pat('hhh',19)
p.show()
c = cat('hhh0',18,'brown')
c.speak()
c.show()
c.show1()