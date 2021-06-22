
# coding: utf-8

# ## 결측치(NaN)를 가지고 연산을 하면 결측치가 된다.

# In[1]:


import pandas as pd


# In[2]:


# 딕셔너리 정의
dict_data = {'c0': [1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔너리를 데이터프레임으로 변환, 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df, '\n')

# 인덱스를 [r0, r1, r2, r3, r4]로 재지정
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf, '\n')

# reindex로 발생한 NaN값을 숫자 0으로 채우기
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2, '\n')

