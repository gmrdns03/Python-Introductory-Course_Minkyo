
A = 0
M = 0
S = 0
G = 0

while True:
	num = int(input("10이상의 수를 입력하세요.[exit: 0 ] >>>>"))
	if num >= 10:
		for i in range(1, num+1):
			if i %3 == 0:
				print("%-2d.  [Apple]"%i)
				A = A + 1
			if i % 8 == 0:
				print("%-2d.  [StrawBarry]"%i)
				M = M + 1
				S = S + 1
			elif i % 4 == 0:
				print("%-2d.  [Melon]"%i)
				M = M + 1
			elif i % 5 == 0:
				print("%-2d.  [Grape]"%i)
				G = G + 1
			else:
				print("%-2d.  -"%i)

		print("="*5, "<< Fruit Count List >>", "="*5)
		print("Apple : %10d회"%A)
		print("Melon: %10d회"%M)
		print("Grape : %10d회"%G)
		print("StrawBerry: %10d회"%S)
		print('='*30)
		break

	elif num == 0:
		print('종료!!')
		break

	else:
		print("^10이상의 숫자를 확인하세요.")
		continue
