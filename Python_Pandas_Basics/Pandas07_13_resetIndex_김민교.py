
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# reset_index

# 딕셔너리 정의
dict_data = {'c0': [1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔너리를 데이터프레임으로 변환, 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df, '\n')

# 행 인덱스를 정수형으로 초기화
ndf = df.reset_index()
print(ndf, '\n')

ndf2 = ndf.reset_index()
print(ndf2, '\n')

