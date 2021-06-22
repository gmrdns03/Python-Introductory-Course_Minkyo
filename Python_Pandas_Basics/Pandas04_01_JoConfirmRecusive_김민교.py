import random

lst = []

def recursive(m):  # 재귀함수 확인하기
	if(chk == len(lst)):
		return
	
	for i in range(m):
		num = random. randint(1, len(name))
		if num not in lst:
			lst.append(num)
		else:
			recursive(chk-len(lst))


while True:
	a = []

	name = input('4인 이상의 이름을 입력하세요.[Space Bar로 구분해주세요, 종료 : 0] :').split()
	if '0' in name:
		exit()

	if len(name) < 4:
		print('\t명수를 확인하세요')
		continue
	
	else:
		for i in name:
			print(i, end = '')
		print('=    %d명 입니다.'%len(name))

		chk = len(name)

		lst = []

		recursive(chk)
		print(lst)
	