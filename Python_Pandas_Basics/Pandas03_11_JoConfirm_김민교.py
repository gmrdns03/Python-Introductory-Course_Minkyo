'''
[조건]
1. 4인 이상 len() 이용해서 인원수 반환
2. 5명 부터 1~5까지 랜덤 숫자 받음
3. 중복없이 반환

sample Run]

'''
import random
import sys

while True:
	a = []

	a = input('4인 이상의 이름을 입력하세요.[종료 : 0] :').split()
	if '0' in a:
		sys.exit()

	if len(a) < 4:
		print('\t명수를 확인하세요')
		continue

	else:
		list01 = []
		print('%d명 입니다.'%len(a))
		while True:
			Ra = random.randint(1,len(a))
			if Ra not in list01:
				list01.append(Ra)
			if len(list01) == len(a):
				break
			else:
				continue
		
		print(list01)
		for i in range(len(a)):
			print("%s번 %s 입니다."%(list01[i], a[i]))    # 번호 각각 붙이기
		print('\t\t\t\t\t\t\t입력되었습니다.')


'''
** for와 재귀함수를 이용한 방법
import random

lst = []

def recursive(m):
	if(chk == len(lst)):
		return
	
	for i in range(m):
		num = random. randint(1, len(name))
		if num not in lst:
			lst.append(num)
		else:
			recursive(chk-len(lst))
	'''
