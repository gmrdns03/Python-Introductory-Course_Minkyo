'''
문제] 
90점 이상이면: A 학점
80점 이상이면: B 학점
70점 이상이면: C 학점
60점 이상이면: D 학점
외에는 : F 학점
'''

Point = 90

if Point >= 90:
	print("A학점")

elif Point >= 80:
	print("B학점")

elif Point >= 70:
	print("C학점")

elif Point >= 60:
	print("D학점")

else:
	print("F학점")