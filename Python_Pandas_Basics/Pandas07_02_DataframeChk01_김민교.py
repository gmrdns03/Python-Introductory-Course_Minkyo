
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


# 열 이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2': [7,8,9], 'c3':[10,11.12], 'c4':[13,14,15]}

# 판다스 DataFrame()함수로 딕셔너리를 데이터 프레임으로 변환
df = pd.DataFrame(dict_data)

# df의 자료형 출력
print(type(df), '\n')

# 변수 df에 저장되어 있는 데이터프레임 객체를 출력
print(df)


# In[8]:


# 행 인덱스/열 이름 지정하여, 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                 index = ['준서', '예은'],
                 columns = ['나이', '성별', '학교'])

# 행 인덱스, 열 이름 확인하기
print(df, "\n")
print(df.index, "\n")
print(df.columns, "\n")

# 행 인덱스, 열 이름 변경하기
df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print(df, '\n')
print(df.index, '\n')
print(df.columns, '\n')


# In[ ]:


# 행 인덱스 / 열 이름 지정하여, 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                 index = ['준서', '예은'],
                 columns = ['나이', '성별', '학교'])

# 데이터프레임 df 출력
print(df, "\n")

redf = df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'})
df.rename(index = {'준서':'학생1', '예은':'학생2'})

# df 출력(변경 후)
print(redf)
print(df)

df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace = True)
df.rename(index = {'준서':'학생1', '예은':'학생2'}, inplace = True)

# df 출력(변경 후)
print(df)

