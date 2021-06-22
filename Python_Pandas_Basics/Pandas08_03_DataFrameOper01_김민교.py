
# coding: utf-8

# ### 데이터 프레임 연산하기
# 
# 여기서는 Seaborn 라이브러리에서 제공하는 데이터셋 중에서
# 타이타닉(titanic) 데이터셋을 사용한다.
# 
# seaborn.load_dataset 함수 확인
# http://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset

# In[2]:


#라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개의 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
print(titanic.columns, "\n", titanic.shape)
df = titanic.loc[:, ['age', 'fare']]
print(df.head(), '\n')
print(type(df), '\n')

# 데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.head(), '\n')
print(type(addition))


# In[3]:


#라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개의 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail(), '\n')
print(type(df), '\n', df.shape)

# 데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.head(), '\n')
print(type(addition), '\n')

# 데이터프레임끼리 연산하기(addition - df)
subtraction = addition - df
print(subtraction.tail(), '\n')
print(type(subtraction))


# ### 결측치 없애보기
# 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html

# In[5]:


#라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개의 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail(), '\n')
print(type(df), '\n', df.shape)

# 데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.head(), '\n')
print(type(addition), '\n')

# 데이터프레임끼리 연산하기(addition - df)
sr_sub = addition.sub(df, fill_value=0)
print(sr_sub.tail(), '\n')
print(type(sr_sub))

