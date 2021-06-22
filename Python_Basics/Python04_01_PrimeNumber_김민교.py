count = 0

while True:
	sosu = int(input('20이상의 수를 입력하세요 [Exit: 0]'))
	if sosu >= 20:
		for i in range(1, sosu+1):
			for j in range(1, i +1):
				if i % j == 0:
					count = count +1
			if count == 2:
				print('%-3d 소수 O'%i)
			else:
				print('%-3d 소수 X'%i)
			count = 0
			continue	
	elif sosu == 0:
		break
	else :
		print("숫자를 확인하세요.")