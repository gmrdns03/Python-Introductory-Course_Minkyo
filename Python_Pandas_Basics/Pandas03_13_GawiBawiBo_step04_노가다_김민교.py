GawiBawiBo = ['가위', '바위', '보']
MenuList = ['1. 가위', '2. 바위', '3. 보', '4. 횟수 입력', '9. 종료']
win = 0
lost = 0
Con = 0

#종료 메시지>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Fini():
	if win > lost:
		print("\t\t\t\t\t총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con, win, lost), '당신이 이겼습니다.', end = '\n\n')
	elif win < lost:
		print("\t\t\t\t\t총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con,win, lost), '당신이 졌습니다.', end = '\n\n')
	else:
		print("\t\t\t\t\t총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Con,win, lost), '비겼습니다.', end = '\n\n')
	print('\t\t\t\t\t<가위바위보    v04>을 종료합니다.', end = '\n\n')

#가위>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def gawi():
	global win
	global lost
	global Con
	ran = random.randint(1,3)
	if ran == 1:
		print('\t\t\t\t\tUser: 가위  /  Com: 가위', '\t', 'draw...', end = '\n\n')
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	if ran == 2:
		print('\t\t\t\t\tUser: 가위  /  Com: 바위', '\t', 'You lost...', end = '\n\n')
		lost += 1
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	if ran == 3:
		print('\t\t\t\t\tUser: 가위  /  Com: 보', '\t', 'You Win!!!', end = '\n\n')
		win += 1
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	Con += 1

#바위>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def bawi():
	global win
	global lost
	global Con
	ran = random.randint(1,3)
	if ran == 1:
		print('\t\t\t\t\tUser: 바위  /  Com: 가위', '\t', 'You Win!!!', end = '\n\n')
		win += 1
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	if ran == 2:
		print('\t\t\t\t\tUser: 바위  /  Com: 바위', '\t', 'draw...', end = '\n\n')
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	if ran == 3:
		print('\t\t\t\t\tUser: 바위  /  Com: 보', '\t', 'You lost...', end = '\n\n')
		lost += 1
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	Con += 1

#보>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def bo():
	global win
	global lost
	global Con
	ran = random.randint(1,3)
	if ran == 1:
		print('\t\t\t\t\tUser: 보  /  Com: 가위', '\t', 'You lost...', end = '\n\n')
		lost += 1
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	if ran == 2:
		print('\t\t\t\t\tUser: 보  /  Com: 바위', '\t', 'You Win!!!', end = '\n\n')
		win += 1
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	if ran == 3:
		print('\t\t\t\t\tUser: 보  /  Com: 보', '\t', 'draw...', end = '\n\n')
		print("\t\t\t\t\t현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(win, lost), end = '\n\n')
	Con += 1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def gawibawibo():
	while True:
		num = input("\t 1, 2, 3 중에서 입력해주세요:  ")
		print()

		if num == "":
			print("Num Chk")
		else:
			num = int(num)

			if num == 1:
				gawi()

			if num == 2:
				bawi()

			if num == 3:
				bo()

			if num == 4:
				print('\t 1, 2, 3 중에서 입력해주세요: ')
				continue

			if num == 9:
				Fini()
				exit()

			if Con == Cnt:
				Fini()
				exit()

			else:
				print('\t 1, 2, 3 중에서 입력해주세요: ')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print('< 가위바위보 v04 >')
print("="*70, end = '\n\n')
for i in MenuList:
	print(i, '\t', end= '')
print()
print("="*70, end = '\n\n')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import random
while True:
	num = input(" 메뉴의 번호를 선택하세요:  ")
	print()

	if num == "":
		print("Num Chk")
	else:
		num = int(num)
		if num == 1:
			gawi()

		if num == 2:
			bawi()

		if num == 3:
			bo()

		if num == 4:
			Con = 0
			Cnt = int(input('\t 게임을 몇번 반복할지 횟수를 입력해주세요: '))
			gawibawibo()
			continue

		if num == 9:
			Fini()
			exit()
	



