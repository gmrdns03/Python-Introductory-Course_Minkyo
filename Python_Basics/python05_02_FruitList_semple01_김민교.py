
answer = []
Fcnt = []



while True:
	n = int(input("10이상의 수를 입력하세요.[exit: 0 ] >>>>"))
	if n >= 10:
		print("=<< %d 번 반복합니다. >>=="%n)
		for i in range(1, n+1):
			if i % 3 == 0:
				answer.append("Apple")
			if i % 4 == 0:
				answer.append("Melon")
			if i %5 == 0:
				answer.append("Grape")
			if i % 8 == 0:
				answer.append("StrawBerry")
			Fcnt = Fcnt + answer

			if len(answer) == 0:
				print("%d."%i)
			else:
				print("%d."% i, str(answer))
			answer = []
	
		print("="*1, "<< Fruit Count List >>", "="*2)
		print("%-10s"%"Apple", ' : ', "%10d회"%Fcnt.count("Apple"))
		print("%-10s"%"Melon", ' : ', "%10d회"%Fcnt.count("Melon"))
		print("%-10s"%"Grape", ' : ', "%10d회"%Fcnt.count("Grape"))
		print("%-10s"%"StrawBerry", ' : ', "%10d회"%Fcnt.count("StrawBerry"))
		print('='*27)
		continue

	elif n == 0:
		print('종료!!')
		break

	else :
		print("^10이상의 숫자를 확인하세요.")
		continue
		