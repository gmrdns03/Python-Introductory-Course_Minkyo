GawiBawiBo = ['가위', '바위', '보']
MenuList = ['1. 가위', '2. 바위', '3. 보', '9. 종료']

win = ()
lost = ()
Con = 0

print('< 가위바위보    v01 >')
print("="*70, end = '\n\n')
for i in MenuList:
	print(i, '\t', end= '')
print()
print("="*70, end = '\n\n')

import random
while True:
	Con += 1
	num = input("\t\t\t\t\t   메뉴의 번호를 선택하세요:  ")

	if num == "":
		print("Num Chk")
	else:
		num = int(num)

	if num == 1:
		ran = random.randint(1, 3)
		if ran == 1:
			print('User: 가위  /  Com: 가위', '\t', 'draw...', end = '\n\n')
		if ran == 2:
			print('User: 가위  /  Com: 바위', '\t', 'You lost...', end = '\n\n')
		if ran == 3:
			print('User: 가위  /  Com: 보', '\t', 'You Win!!!', end = '\n\n')
		continue

	if num == 2:
		ran = random.randint(1, 3)
		if ran == 1:
			print('User: 바위  /  Com: 가위', '\t', 'You Win!!!', end = '\n\n')
		if ran == 2:
			print('User: 바위  /  Com: 바위', '\t', 'draw...', end = '\n\n')
		if ran == 3:
			print('User: 바위  /  Com: 보', '\t', 'You lost...', end = '\n\n')
		continue

	if num == 3:
		ran = random.randint(1, 3)
		if ran == 1:
			print('User: 보  /  Com: 가위', '\t', 'You lost...', end = '\n\n')
		if ran == 2:
			print('User: 보  /  Com: 바위', '\t', 'You Win!!!', end = '\n\n')
		if ran == 3:
			print('User: 보  /  Com: 보', '\t', 'draw...', end = '\n\n')
		continue

	if num == 9:
		print('<가위바위보    v01>을 종료합니다.', end = '\n\n')
		break
		exit()

	else:
		print("\t\t\t\t"," 계속하려면 메뉴 번호를 확인하세요", end = '\n\n')
		

	



