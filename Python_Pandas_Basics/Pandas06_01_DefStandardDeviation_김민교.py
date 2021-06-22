
# coding: utf-8

# In[8]:


import pandas as pd
datalist = [28,31,24,25,30,32,20,30,31,26,31,40,37,27]
print('관측값:', datalist)

# 평균 구하는 함수 만들기
def mMean():
    hab = 0
    for i in datalist:
        hab += i
    return hab/len(datalist)

print('평균: ', mMean())

# 편차
def mDeviation():
    Devi = []
    Mean = mMean()
    for i in datalist:
        Devi.append(round(i-Mean, 2))
    return Devi

print('편차: ', mDeviation())

# 분산
def mVariance():
    jegobhab = 0
    devi = mDeviation()
    for i in devi:
        jegobhab += i**2
    return jegobhab/(len(datalist)-1)
    
print('분산: ', mVariance())


# In[10]:


# 표준편차(Standard Deviation) : 분산의 제곱근
def mStandardDeviation():
    Vari = mVariance()
    return Vari**(1/2)
print('표준편차:', mStandardDeviation())

# 범위(Range) : 최댓값과 최솟값의 차이
def mRange():
    datalist02 = pd.Series(datalist)
    return datalist02.max() - datalist02.min()
print('범위: ', mRange())

