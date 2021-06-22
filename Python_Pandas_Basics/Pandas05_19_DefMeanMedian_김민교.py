
# coding: utf-8

# In[28]:


datalist = [28,31,24,25,30,32,20,30,31,26,31]
print(datalist)


# In[29]:


# 평균 구하는 함수 만들기
def mMean():
    hab = 0
    for i in datalist:
        hab += i
    return hab/len(datalist)

print(mMean())
    
# 중앙값 구하는 함수 만들기
def mMedian():
    datalist.sort()
    if len(datalist)%2 == 1:
        a = (len(datalist)+1/2)-1
        return datalist[int(a)]
    else:
        b = len(datalist)/2 -1
        c = (len(datalist)/2 + 1) -1
        d = (datalist[int(b)]+datalist[int(c)])/2
        return d
    
print(mMedian())

