#다중 for문

for i in range(2,4):
	print('Outer : ', i)
	for j in range (1,5):
		print('Inner : ', j , end= "\t")
	print(end = '')