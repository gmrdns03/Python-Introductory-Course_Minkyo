GawiBawiBo = ['가위', '바위', '보']
MenuList = ['1. 가위', '2. 바위', '3. 보', '4. 횟수 입력', '9. 종료']
win = 0
lost = 0
Con = 0

print('< 가위바위보 v04 >')
print("="*70, end = '\n\n')
for i in MenuList:
	print(i, '\t', end= '')
print()
print("="*70, end = '\n\n')

import random
while True:
	num = input("\t\t\t\t\t   메뉴의 번호를 선택하세요:  ")

	if num == "":
		print("Num Chk")
	else:
		num = int(num)
		if num == 1:
			ran = random.randint(1,3)
			if ran == 1:
				print('User: 가위  /  Com: 가위', '\t', 'draw...', end = '\n\n')
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			if ran == 2:
				print('User: 가위  /  Com: 바위', '\t', 'You lost...', end = '\n\n')
				lost += 1
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			if ran == 3:
				print('User: 가위  /  Com: 보', '\t', 'You Win!!!', end = '\n\n')
				win += 1
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			Con += 1

		if num == 2:
			ran = random.randint(1,3)
			if ran == 1:
				print('User: 바위  /  Com: 가위', '\t', 'You Win!!!', end = '\n\n')
				win += 1
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			if ran == 2:
				print('User: 바위  /  Com: 바위', '\t', 'draw...', end = '\n\n')
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			if ran == 3:
				print('User: 바위  /  Com: 보', '\t', 'You lost...', end = '\n\n')
				lost += 1
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			Con += 1

		if num == 3:
			ran = random.randint(1,3)
			if ran == 1:
				print('User: 보  /  Com: 가위', '\t', 'You lost...', end = '\n\n')
				lost += 1
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			if ran == 2:
				print('User: 보  /  Com: 바위', '\t', 'You Win!!!', end = '\n\n')
				win += 1
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			if ran == 3:
				print('User: 보  /  Com: 보', '\t', 'draw...', end = '\n\n')
				print("현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
			Con += 1

		if num == 4:
			Cnt = input()
			continue
'''
		elif Con == Cnt:
			if win > lost:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con, win, lost), '당신이 이겼습니다.', end = '\n\n')
			elif win < lost:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con,win, lost), '당신이 졌습니다.', end = '\n\n')
			else:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con,win, lost), '비겼습니다.', end = '\n\n')
			print('<가위바위보    v04>을 종료합니다.', end = '\n\n')
'''	
		if num == 9:
			if win > lost:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con, win, lost), '당신이 이겼습니다.', end = '\n\n')
			elif win < lost:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con,win, lost), '당신이 졌습니다.', end = '\n\n')
			else:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con,win, lost), '비겼습니다.', end = '\n\n')
			print('<가위바위보    v04>을 종료합니다.', end = '\n\n')
			exit()