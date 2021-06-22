
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns


# In[3]:


# 1. 행렬정보 확인
titanic = sns.load_dataset('titanic')
print('='*40, 'head', '='*40)
print(titanic.head())
print('='*40, 'tail', '='*40)
print(titanic.tail())
print('='*40, 'shape', '='*40)
print(titanic.shape)
print('='*40, 'info', '='*40)
print(titanic.info())


# In[4]:


# 2. 컬럼명 확인하기
print(titanic.columns)
print(len(titanic.columns))


# In[5]:


# 3. 각 컬럼별 유닉크한 값 구하기
for idx in titanic.columns:
    print(f'{idx}')
    print(titanic[idx].unique())
    print('='*40)


# In[6]:


# 3. 각 컬럼별 유닉크한 값 구하기
titanic_col_List = titanic.columns
for i in titanic_col_List:
    print(f'{i}의 유니크 값 리스트 \n {titanic[i].unique()}')
    print('='*80)

