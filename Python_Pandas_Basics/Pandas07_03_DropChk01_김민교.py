
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:



# DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
exam_data = {'수학' :[90,80,70], '영어': [98,89,95], '음악': [85,95,100], '체육': [100,90,90]}

df = pd.DataFrame(exam_data)
print(df, '\n')

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df, '\n')

# 데이터프레임 df를 복제하여 변수 df2에 저장, df2의 1개 행을 삭제
df2 = df[:]
df2.drop('우현', inplace=True)
print(df2, '\n')

# 데이터프레임 df를 복제하여 변수 df3에 저장, df의 2개 행을 삭제
df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True)
print(df3)

#데이터프레임 df를 복제하여 변수 df4에 저장, df4의 1개 열을 삭제
df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4, '\n')

# 데이터프레임 df를 복제하여 변수 df5에 저장, df5의 2개 열을 삭제
df5 = df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)

