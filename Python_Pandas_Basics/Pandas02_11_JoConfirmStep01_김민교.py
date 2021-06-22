'''
input()함수 이용
결과: 4인 이상의 이름을 입력하세요(SB로 구분한다.):보라돌이 나나
- 4인이 아니면 --> 명수를 확인하세요
- 4인 이상이면 --> 보라돌이 나나 뚜비 뽀오 입력되었습니다.
...
'''
i = []
result = input('4인 이상의 이름을 입력하세요 : ') # >>>0넣었을 때 종료 만들어야 함

i = result.split()

if len(i) >= 4:
	for j in i:
		print(j, end = '')
	print('입력되었습니다.')

if result == 0:
	exit()
else:
	print('명수를 확인하세요.')