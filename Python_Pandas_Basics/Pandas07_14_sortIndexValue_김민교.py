
# coding: utf-8

# In[1]:


import pandas as pd

# 딕셔너리 정의
dict_data = {'c0': [1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔너리를 데이터프레임으로 변환, 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df, '\n')


# In[9]:


# sort_index
# ascending의 디폴트 값은 True(오름차순)으로 되어있다.
# axis=0이면 인덱스가 순서대로 바뀌고, axis=1이면 컬럼이 순서대로 바뀐다.
ndf = df.sort_index(axis=1, ascending=False)
print(ndf)


# In[18]:


# sort_values
ndf2 = df.sort_values(by='c1', ascending=False)
ndf3 = df.sort_values(by = ['c4',  'c3',  'c2',  'c1',  'c0'], axis = 1, ascending=False)
print(ndf2)
print(ndf3)

