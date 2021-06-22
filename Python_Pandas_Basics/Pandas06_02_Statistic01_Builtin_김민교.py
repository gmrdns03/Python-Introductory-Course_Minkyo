
# coding: utf-8

# In[2]:


import pandas as pd

datalist = [28,31,24,25,30,32,20,30,31,26,31]


# In[12]:


da = pd.Series(datalist)

print(f"Built_in 정렬 sort_values() :  \n{da.sort_values(ascending=True)}")
print("="* 60)
print(f"Built_in 평균 mean() : {da.mean()}")
print(f"Built_in 중위수 median() : {da.median()}")
print(f"Built_in 분산 var() : {da.var()}")
print(f"Built_in 표준편차 std() : {da.std()}")
print(f"Built_in 제 1사분위수 quantile() : {da.quantile(q= 0.25)}")
print(f"Built_in 제 2사분위수 quantile() : {da.quantile(q= 0.50)}")
print(f"Built_in 제 3사분위수 quantile() : {da.quantile(q= 0.75)}")
      
print("="* 60) 
da.describe()
      

