
add = 0
for i in range(1, 11):
	add = add + i
print('1 - 10 까지의 합 : ', add)

# 1~10 까지 홀수합 출력 !!
odd = 0
for i in range(1, 11, 2):
	odd = odd + i
print(' 1~10 까지 홀수 합 : ', odd)

# 1~10까지 짝수 합 출력 !!
even = 0
for i in range(2, 11, 2):
	even = even + i
print(' 1~10 까지 짝수 합 : ', even)