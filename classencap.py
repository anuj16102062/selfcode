class polygon:
	__w = None## these are private member of the class inhe clas ke nbahar call mhi kar sakte iske get_fun use kare 
	__h = None
	def set_values(self,w,h):
		self.__w = w
		self.__h = h
	def get_w(self):
		
		return self.__w
	def get_h(self):
		return self.__h
class rect(polygon):
	def area(self):
		return self.get_w() * self.get_h()
r = rect()
r.set_values(50,40)
p = polygon()
print(r.area())
class polygo:
	def __init__ (self,width,height):
		self.width = width
		self.height = height
	def show(self):
		print(f"{self.width},{self.height}")
class rec(polygo):
	def __init__ (self,width,height,length):
		self.length = length
		super(). __init__ (width,height)
	def area(self):
		return self.width * self.height * self.length

p = polygo(50,68)
r = rec(50,68,4)
p.show()
print(r.area())
