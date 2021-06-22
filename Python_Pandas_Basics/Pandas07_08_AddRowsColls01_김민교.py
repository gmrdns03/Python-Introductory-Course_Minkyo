
# coding: utf-8

# In[2]:


import pandas as pd

exam_data = {'이름':['서준', '우현', '인아'],
             '수학' : [90,80,70], 
             '영어' : [98,89,95], 
             '음악': [85,95,100], 
             '체육': [100,90,90]}

df = pd.DataFrame(exam_data)
print(df, '\n')


# In[3]:


# 데이터프레임 df에 '국어' 점수 열을 추가, 데이터 값은 80지정
df['국어'] = 80
print(df)


# In[6]:


# 새로운 행 추가_ 같은 원소 값을 입력
df.loc[3] = 0
print(df, '\n')

# 새로운 행을 추가_원소 값 여러개의 배열 입력
df.loc[4] = ['동규', 90,80,70,60, 80]
print(df, '\n')

# 새로운 행을 추가_ 기존 행을 복사
df.loc['행5'] = df.loc[3]
print(df)

