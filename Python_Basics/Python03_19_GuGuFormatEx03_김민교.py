
for i in range(2,10):
	print("# %s단" %i, end='        ')
print()

print('-' * 100)
for i in range(2,10):
	for j in range(2,10):
		print(j, 'x', i, '=', '%3d'%(j*i), end='  ')
	print('\n')
print('-' * 100)

print('\n')

for i in range(2,10):
	print("# %s단" %i, end='      ')
print()

print('-' * 100)
for i in range(2,10):
	for j in range(2,10):
		print('%dx%d ='%(j,i), '%3d'%(j*i), end='  ')
	print()
print('-' * 100)

'''
1. 몇 행/ 몇 열인지 확인
    행(아우터)/ 열(이너)
'''

