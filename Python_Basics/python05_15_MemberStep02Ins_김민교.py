
# 1 2 3 9 이외에는 숫자 확인하세요 메시지 띄우기

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
memList = []
d = []
dt = []

print("="*20, '메뉴선택', "="*20, end = '\n\n')
print("{0} {1} {2} {3}".format(menu[0], menu[1], menu[2], menu[3]), end = '\n\n')
print("="*50, end = '\n\n')

while True:
	num = input('메뉴의 번호를 선택해주세요. :  ')

	if num == "":
		print("Chk", end = '')
	else:
		num = int(num)

	if num == 1:
		print("\t","{}".format(menu[0]), end = '\n\n')
		for i in range(0, len(itemList)):
			print(itemList[i], ':', end = '')
			d.append(input())
		memList.append(d)
		print(memList)	
		print('현재 회원 수는 총 : ', len(memList), '명 입니다.')
	elif num == 2:
		print("\t",menu[1], "Algorithm Chk", end = '\n\n')
	elif num == 3:
		print("\t",menu[2], "Algorithm Chk", end = '\n\n')
	elif num == 9:
		print("\t",menu[3], end = '\n\n')
		break
	else:
		print("\t","메뉴 번호를 확인하세요", end = '\n\n')
		

