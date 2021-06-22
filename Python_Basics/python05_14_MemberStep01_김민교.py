
# 1 2 3 9 이외에는 숫자 확인하세요 메시지 띄우기

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']

print("="*20, '메뉴선택', "="*20, end = '\n\n')
print('1. 회원가입  2. 로그인  3. 회원목록  9. 메뉴종료', end = '\n\n')
print("="*50, end = '\n\n')



while True:
	num = input('메뉴의 번호를 선택해주세요. :  ')
	if num == "":
		print("Chk")
	else:
		num = int(num)

	if num == 1:
		print("\t",menu[0], end = '\n\n')
	elif num == 2:
		print("\t",menu[1], end = '\n\n')
	elif num == 3:
		print("\t",menu[2], end = '\n\n')
	elif num == 9:
		print("\t",menu[3], end = '\n\n')
		break
	else:
		print("\t","메뉴 번호를 확인하세요", end = '\n\n')
		

