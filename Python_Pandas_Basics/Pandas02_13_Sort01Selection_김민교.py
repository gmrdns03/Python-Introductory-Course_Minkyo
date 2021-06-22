'''
** Selection Sort
	1. 오름차순
		숫자: 작은 수 --> 큰 수
		영문: A --> Z
		한글: ㄱ --> ㅎ

	2. 내림차순
		숫자: 큰 수 --> 작은 수
		영문: Z --> A
		한글: ㅎ --> ㄱ

전처리: 인덱싱, 슬라이싱, Sort

교환 알고리즘
a =10
b = 20
==========
c(=a') = a  
a(=b') = b
b(=a') = c(=a')j
=============
i[a], i[b] = i[b], i[a]
'''

i = [2, 5, 6, 1, 2, 8, 33, 77, 12]


'''
# 기본 교환 알고리즘 원리
for a in range(0, len(i)):
	for b in range(a+1, len(i)):
		if int(i[a]) > int(i[b]):
			 c =int(i[a])
			 i[a] = int(i[b])
			 i[b] = c
		else:
			pass
print(i)
'''

# 파이썬에서만 가능한 교환 알고리즘
for a in range(0, len(i)):
	for b in range(a+1, len(i)):
		if i[a] > i[b]:
			i[a], i[b] = i[b], i[a]
		else:
			pass
print(i)
i.reverse()
print(i)
