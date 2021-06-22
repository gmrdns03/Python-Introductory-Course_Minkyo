num = int(input('숫자를 입력해주세요:'))

if num >= 10:
	for i in range(1, num+1):
		if i % 3 == 0:
			print