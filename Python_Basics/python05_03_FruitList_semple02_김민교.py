N = int(input("10이상의 수를 입력하세요.[exit: 0 ] >>>>"))
fruitList = ["Apple", "Melon", "Grape", "StrawBerry"]
fruitNumber = [3, 4, 5, 8]
fruitCount = [0, 0, 0, 0]

print("=<< %d 번 반복합니다. >>=="%N)
for i in range(1, N+1):
	print("\n%2d." %i, end = "")
	for j in range(len(fruitList)):  #왜 len(fruitList)를 쓰는겨: fruitList에 인덱스값을 찾으려고
		if(i % fruitNumber[j] == 0):
			fruitCount[j] += 1
			print("%s"% fruitList[j], end=' ')

print("\n\n==<<Fruit Count List >> ==")
for i in range(len(fruitList)):
	print("%d. %-12s %2d회" % (i + 1, fruitList[i], fruitCount[i]))
