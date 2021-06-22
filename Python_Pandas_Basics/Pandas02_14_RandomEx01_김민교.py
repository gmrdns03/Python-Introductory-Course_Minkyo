
print('랜덤 숫자 불러오기 ver001')

import random

for i in range(5):
	print("%f "%random.random(), end = '')

print("\n", '-'*50, '\n')

for i in range(5):
	print('%d '%random.randint(1, 3), end = '')

print("\n", '-'*50, '\n')

for i in range(5):
	print('%d '%random.randint(1, 45), end = '')
	print()