dev=[]


while True:
	num = int(input("10이상의 수를 입력하세요.[exit: 0 ]>>>>"))
	if num >= 10:
		for i in range(1, num+1):
			if i %3 == 0:
				print("%-2d.  [Apple]"%i)
				
			elif i % 8 == 0:
				print("%-2d.  [Melon, StrawBarry]"%i)
				 
			elif i % 4 == 0:
				print("%-2d.  [Melon]"%i)
				 
			elif i % 5 == 0:
				print("%-2d.  [Grape]"%i)
				 
			else:
				print("%-2d.  -"%i)
		print(dev)
		break
	else:
		print("^10이상의 숫자를 확인하세요.")
		continue
