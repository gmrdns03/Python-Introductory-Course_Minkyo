class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		result = self.first + self.second
		return result

	def sub(self):
		result = self.first - self.second
		return result
	
	def mul(self):
		result = self.first * self.second
		return result
	
	def div(self):
		result = self.first / self.second
		return result

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)

print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())
print()
print(b.sum())
print(b.sub())
print(b.mul())
print(b.div())