'''
# 매개변수에 초깃값 미리 설정하기
	say_myself 함수는 3개의 매개변수를 받아서 마지막 인수인
	man이 True이면 '남자입니다', false면 '여자입니다' 출력
'''

def say_myself(name, old, man=True):      # man이 True라는 디폴트 값 설정
	print('나의 이름은 %s입니다.'% name)
	print('나이는 %d살 입니다.'%old)
	if man:
		print('남자입니다.')
	else:
		print('여자입니다.')

say_myself('소나무', 27) # 기본값이 man=True이기 때문에 설정을 안해주면 '남자입니다.'가 프린트된다.
print("_"*20)

say_myself('오렌지', 25, False)
print("_"*20)