class FourCal:
	def __init__(self):
		pass
	def __init__(self, first, second):
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

'''
def setdata(self, first, second):
		self.first = first
		self.second = second
'''
	
# a= FourCal()
# a.setdata(4, 2)

a = FourCal(4, 2)

print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())