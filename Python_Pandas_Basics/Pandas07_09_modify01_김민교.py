
# coding: utf-8

# In[1]:


import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학' : [90,80,70], 
             '영어' : [98,89,95], 
             '음악': [85,95,100], 
             '체육': [100,90,90]}

df = pd.DataFrame(exam_data)
print(df, '\n')


# In[2]:


# '이름'열을 새로운 인덱스로 지정하고, df객체에 변경사항 반영
df.set_index('이름', inplace = True)
print(df, '\n')

# 데이터프레임 df의 특정 원소를 변경하는 방법 3개
df.iloc[0][3] = 80
print(df, '\n')

df.loc['서준']['체육'] = 90
print(df, '\n')

df.loc['서준', '체육'] = 100
print(df, '\n')

