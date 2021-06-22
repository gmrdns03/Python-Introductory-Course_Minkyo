
# coding: utf-8

# In[1]:


import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학' : [90,80,70], 
             '영어' : [98,89,95], 
             '음악': [85,95,100], 
             '체육':[100,90,90]}

df = pd.DataFrame(exam_data)
print(df, '\n')

# '이름'열을 새로운 인덱스로 지정하고, df객체에 변경사항 반영
df.set_index('이름', inplace = True)
print(df, '\n')

# 데이터프레임 df의 특정 원소 1개 선택('서준'의 '음악'점수)
a = df.loc['서준', '음악']
print(a, '\n')
b = df.iloc[0,2]
print(b, '\n')


# In[4]:


# 데이터프레임 df의 특정 원소 2개 이상 선택('서준'의 '음악', '체육'점수)
c = df.loc['서준', ['음악', '체육']]
print(c, '\n')

d = df.iloc[0, [2,3]]
print(d, '\n')

e = df.loc['서준', '음악':'체육']
print(e,'\n')

f = df.iloc[0, 2:]
print(f,'\n')

# df의 2개 이상의 행과 열로부터 원소 선택('서준', '우현'의 '음악','체육'점수)
g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g,'\n')

h = df.iloc[[0,1], [2,3]]
print("df.iloc[[0,1], [2,3]]\n", h, '\n')

i = df.loc['서준':'우현', '음악':'체육']
print("df.loc[['서준':'우현'], ['음악':'체육']]\n", i, '\n')

j = df.iloc[0:2, 2:]
print(j)






