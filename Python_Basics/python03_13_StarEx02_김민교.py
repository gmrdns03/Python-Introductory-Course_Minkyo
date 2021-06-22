for i in range(0,6):
	print('*'*(6-i))

for i in range(1,6):           #1           2         3      4    5
	for j in range(0,6-i):    #01234   0123   012   01  0
		print('*', end = '')
	print('')

count = int(input("열 갯수를 입력해주세요 : "))

for i in range(count, 0 , -1):
	for j in range(i):
		print('*', end= '')
	print()

'''
- range()
- range(stop)
- rnage(start, stop, [step])   <<--step= 단계( + - )
- 오버로드(Overload): 같은 이름의 함수가 여러 용도로 쓰이는 것
		                          :매개변수의 타입, 개수
- 함수에 들어가는 수= 매개변수


