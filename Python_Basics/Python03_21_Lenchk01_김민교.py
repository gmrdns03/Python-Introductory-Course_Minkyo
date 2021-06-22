list01 = [70,60,55,75,95,90,80,85,100]
print(len(list01))
sum = 0
for junsu in list01:
	sum = sum + junsu

print('합계: ', sum)
print('평균: ', '%0.2f'%(sum/len(list01)))