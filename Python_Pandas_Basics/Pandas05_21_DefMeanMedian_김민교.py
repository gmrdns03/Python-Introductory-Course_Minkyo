
# coding: utf-8

# In[1]:


datalist = [28,31,24,25,30,32,20,30,31,26,31,40,37,27]
print(datalist)


# In[2]:


# 평균 구하는 함수 만들기
def mMean():
    hab = 0
    for i in datalist:
        hab += i
    return hab/len(datalist)

print(mMean())


# In[3]:


def mDeviation():
    Devi = []
    Mean = mMean()
    for i in datalist:
        Devi.append(round(i-Mean, 2))
    return Devi


# In[8]:


def mVariance():
    jegobhab = 0
    devi = mDeviation()
    for i in devi:
        jegobhab += i**2
    return jegobhab/(len(datalist)-1)
    
print(mVariance())

