# lambda 활용법

x = lambda a : a+ 10
print(x(5))

x = lambda a, b : a*b
print(x(5,6))

def myfunc(n):
	return lambda a : a* n

mydoubler = myfunc(2)				#mydoubler = lambda a: 2*a
print(mydoubler(11))					#11이 --> a라는 변수에 들어가서 출력된다.

def myfunc(n):
	return lambda a : a* n

mydoubler = myfunc(3)
print(mydoubler(11))