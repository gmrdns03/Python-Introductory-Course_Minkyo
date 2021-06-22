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

class SafeFourCal(FourCal):  # 현재 매소드를 우선한다.
	def div(self):
		if self.second == 0:
			return 0
		else:
			return FourCal.div(self) # super().div()는 상위 클래스를 의미한다. / return FourCal.div(self)로 직접 상위 클래스를 소환해도 됨

a = SafeFourCal(4, 7)  # 호출한 현재 매소드를 우선한다. ↑↑↑↑

print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())
print()
print(a.first, '+', a.second, '=', a.sum())
print(a.first, '-', a.second, '=', a.sub())
print(a.first, '*', a.second, '=', a.mul())
print(a.first, '/', a.second, '=', a.div())
print()
print("%d + %d = %d"%(a.first, a.second, a.sum()))
print("%d - %d = %d"%(a.first, a.second, a.sub()))
print("%d * %d = %d"%(a.first, a.second, a.mul()))
print("%d / %d = %0.2f"%(a.first, a.second, a.div()))
print()
print("{} + {} = {}".format(a.first, a.second, a.sum()))
print("{} - {} = {}".format(a.first, a.second, a.sub()))
print("{} * {} = {}".format(a.first, a.second, a.mul()))
print("{} / {} = {:0.2f}".format(a.first, a.second, a.div()))
print()
print(f"{a.first} + {a.second} = {a.sum()}")
print(f"{a.first} - {a.second} = {a.sub()}")
print(f"{a.first} * {a.second} = {a.mul()}")
print(f"{a.first} / {a.second} = {a.div():0.2f}")