
# coding: utf-8

# In[4]:


import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학' : [90,80,70], 
             '영어' : [98,89,95], 
             '음악': [85,95,100], 
             '체육': [100,90,90]}

df = pd.DataFrame(exam_data)
print(df, '\n')

df.set_index('이름', inplace=True)


# In[5]:


# 데이터 프레임 df의 원소 여러개를 변경하는 방법
df.loc['서준', ['음악', '체육']] = 50
print(df, '\n')

# 데이터프레임 df를 전치하기(메소드 활용)
df = df.transpose()
print(df, '\n')

# 데이터프레임 df를 다시 전치하기(클래스 속성 활용)
df = df.T
print(df, '\n')

