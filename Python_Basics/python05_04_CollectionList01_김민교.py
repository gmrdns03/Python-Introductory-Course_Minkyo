'''
collection Data type: 1개 이상의 값을 저장.

List 형-- 내부적으로 인덱스를 관리해주는
				인덱스로 정리해두기 때문에 정리O --> 중복 됨
				--> List 형을 많이 사용한다.

Set 형-- 정리X --> 중복 안됨

Dictionary 형 -- 처음부터 키값과 벨류 값을 함께 넣어놓는다.
						  List형과 set형의 복합
						  키값은 Set형 --> 중복 안됨
						  벨류값은 List형--> 중복 됨

튜플형 -- unchangerable

'''
# 비어있는 리스트는 a = list()로 생성할 수도 있다.

a = [1,2,3]
print(a[0])
print(a[0] + a[2])
print(a[-1])
print("-" * 15)

e = [1, 2, ['Life', 'is']]
print(e[-1])
print(e)

'''
a = [] 
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
'''