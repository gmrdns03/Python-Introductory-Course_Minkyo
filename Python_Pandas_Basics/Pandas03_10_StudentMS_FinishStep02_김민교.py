#DictionaryEx

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3', '4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;
a = []

def inputData():
	for i in range(len(idList)):
		dic[idList[i]] = scoreList[i]

# 1번 메뉴 알고리즘-------------------------------------------------------------------------------------
# 01. 해당하는 아이디 없는 경우 --> "^    해당하는 아이디 없음"
# 02. 해당하는 아이디 있는 경우: deleteIDList = []에 넣기
# 03. 해당하는 아이디 있는 경우: 삭제
def DelID():
	Id = input('ID를 입력해주세요.:  ')
	if Id in idList:
		del dic[Id] 
		deleteIDList.append(Id)
		print("{}가 삭제되었습니다.".format(Id))
		print(deleteIDList)
	else:
		print('^ 해당하는 아이디가 없습니다.')

# 2번 메뉴 알고리즘-------------------------------------------------------------------------------------
# 01. ID입력받는다 >>>>>탈퇴 경력 O>>>>>"탈퇴회원 가입 불가"
# 02. ID입력받는다 >>>>>중복ID있음>>>>>"^    중복 아이디 있음"
# 03. ID입력받는다 >>>>>탈퇴 경력 X>>>>>중복ID없음 >>>>>가입절차
# 04. 4개 값, ID, 필기, 실기, 인성 받기
Score = []
def SignIn():
	loginId = input('ID를 입력해주세요. : ')
	if loginId in deleteIDList:  
		print("탈퇴회원 가입 불가")
	elif loginId in dic.keys():
		print("^    이미 회원입니다.")
	else:
		print("ID 추가 등록을 진행합니다.")
		for num in range(4):
			if num == 0:
				print(MenuList[num], ':', end = '')
				idList.append(input())
			else:
				print(MenuList[num], ':', end = '')
				Score.append(int(input()))
		scoreList.append(Score)
		dic[idList[-1]] = scoreList[-1]

# 3번 메뉴 알고리즘-------------------------------------------------------------------------------------
PassPeople = []
def PrintList():
	for i in MenuList:
		print(i, '\t', end = '')
	print('')

	print("="*70, end = '\n')
	for j in dic.keys():
			if sum(dic[j][0:3])/3 >= 70:
				print("%-7s %-7s %-7s %-7s %-7s %-7.2f %-7s"%(j, dic[j][0], dic[j][1], dic[j][2], sum(dic[j][0:3]), sum(dic[j][0:3])/3, '합격'), end = '\n')
			else:
				print("%-7s %-7s %-7s %-7s %-7s %-7.2f %-7s"%(j, dic[j][0], dic[j][1], dic[j][2], sum(dic[j][0:3]), sum(dic[j][0:3])/3, '불합격'), end = '\n')
	
	print("="*70, end = '\n')


# 4번 메뉴 알고리즘-------------------------------------------------------------------------------------
# 일단 PassChk()라는 함수를 이용해서 만들기
def PassList():
	print("합격생 목록: ", end = '')
	for Pas in dic.keys():
		if sum(dic[Pas][0:3])/3 >= 70 :
			PassPeople.append(Pas)
			print(Pas, end =' ')
		else:
			pass
	print(end = '\n\n')

# 9번 메뉴 알고리즘-------------------------------------------------------------------------------------
def Exit():
	print('\t',menu[4], end = '\n')
	print('\t\t\t\t\t\t\t    ', "종료합니다.")

# -------------------------------------------------------------------------------------------------------------
print('학생관리시스템v01')
print("="*70, end = '\n\n')
for i in menu:
	print(i, end = '')
print('\n')
print("="*70, end = '\n\n')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
inputData()
while True:
	num = input("\t\t\t\t\t   메뉴의 번호를 선택하세요:  ")
	print('')

	if num == "":
		print("Chk", end = '')
	else:
		num = int(num)

# 1번 메뉴-------------------------------------------------------------------------------------
	if num == 1:
		DelID()

# 2번 메뉴-------------------------------------------------------------------------------------
	if num == 2:
		SignIn()

# 3번 메뉴-------------------------------------------------------------------------------------
	if num == 3:
		PrintList()

# 4번 메뉴-------------------------------------------------------------------------------------
	if num == 4:
		PassList()

# 9번 메뉴-------------------------------------------------------------------------------------
	if num == 9:
		Exit()
		break

# 예외-------------------------------------------------------------------------------------
	else:
		print("\t\t\t\t"," 계속하려면 메뉴 번호를 확인하세요", end = '\n\n')

