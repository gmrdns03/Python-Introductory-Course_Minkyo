
# coding: utf-8

# In[1]:


datalist = [28,31,24,25,30,32,20,30,31,26,31]
print(datalist)


# In[2]:


# 평균 구하는 함수 만들기
def mMean():
    hab = 0
    for i in datalist:
        hab += i
    return hab/len(datalist)

print(mMean())


# In[12]:


def mDeviation():
    Devi = []
    Mean = mMean()
    for i in datalist:
        Devi.append(i-Mean)
    return Devi
    


# In[13]:


print(mDeviation())

