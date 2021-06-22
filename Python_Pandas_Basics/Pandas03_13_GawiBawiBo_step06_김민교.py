GawiBawiBo = ['가위', '바위', '보']
MenuList = ['1. 가위', '2. 바위', '3. 보', '4. 횟수입력', '9. 종료']

#========================================================================================
def gawibawibo():
	win = 0 ; lost = 0 ; Cnt = 0 ; num = 0
	while True:
		num = input('메뉴의 번호를 입력해주세요: ')
		if num not in (1, 2, 3, 9):
			continue

		print()
		ran = random.randint(1,3)

		if num == "":
			print('Chk Num')
		else:
			num = int(num)

		if num - ran == -1 or num - ran == 2:
			lost += 1
			Cnt += 1
			print('USER: {}  :   COM: {}  -->  당신이 졌습니다.'.format(GawiBawiBo[num-1], GawiBawiBo[ran-1]))
			print()

		if num - ran == -2 or num - ran == 1:
			win += 1
			Cnt += 1
			print('USER: {}  :   COM: {}  -->  당신이 이겼습니다.'.format(GawiBawiBo[num-1], GawiBawiBo[ran-1]))
			print()

		if num - ran == 0:
			Cnt += 1
			print('USER: {}  :   COM: {}  -->  무승부입니다.'.format(GawiBawiBo[num-1], GawiBawiBo[ran-1]))
			print()

		if num == 9 or Cnt == Cnt02:
			if win > lost:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Cnt, win, lost), '당신이 이겼습니다.', end = '\n\n')
			elif win < lost:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Cnt,win, lost), '당신이 졌습니다.', end = '\n\n')
			else:
				print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Cnt,win, lost), '비겼습니다.', end = '\n\n')
			print('<가위바위보    v06>을 종료합니다.', end = '\n\n')
			exit()
#메뉴 보드=============================================================================================
print('< 가위바위보    v06 >')
print("="*70, end = '\n\n')
for i in MenuList:
	print(i, '     ', end= '')
print()
print()
print("="*70, end = '\n\n')

#메인틀 =============================================================================================
import random
win = 0 ; lost = 0 ; Cnt = 0 ; num = 0
while True:
	num = input('메뉴의 번호를 입력해주세요: ')
	if num not in (1, 2, 3, 9):
			continue
	print()
	ran = random.randint(1,3)

	if num == "":
		print('Chk Num')
	else:
		num = int(num)

	if num == 4:
		Cnt02 = int(input('게임을 몇번 반복하시겠습니까?:  '))
		gawibawibo()

	if num - ran == -1 or num - ran == 2:
		lost += 1
		Cnt += 1
		print('USER: {}  :   COM: {}  -->  당신이 졌습니다.'.format(GawiBawiBo[num-1], GawiBawiBo[ran-1]))
		print()

	if num - ran == -2 or num - ran == 1:
		win += 1
		Cnt += 1
		print('USER: {}  :   COM: {}  -->  당신이 이겼습니다.'.format(GawiBawiBo[num-1], GawiBawiBo[ran-1]))
		print()

	if num - ran == 0:
		Cnt += 1
		print('USER: {}  :   COM: {}  -->  무승부입니다.'.format(GawiBawiBo[num-1], GawiBawiBo[ran-1]))
		print()

	if num == 9:
		if win > lost:
			print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Cnt, win, lost), '당신이 이겼습니다.', end = '\n\n')
		elif win < lost:
			print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Cnt,win, lost), '당신이 졌습니다.', end = '\n\n')
		else:
			print("총 %s회 게임 중 현재 스코어 %s : %s (당신 : 컴퓨터) 입니다."%(Cnt,win, lost), '비겼습니다.', end = '\n\n')
		print('<가위바위보    v06>을 종료합니다.', end = '\n\n')
		break

