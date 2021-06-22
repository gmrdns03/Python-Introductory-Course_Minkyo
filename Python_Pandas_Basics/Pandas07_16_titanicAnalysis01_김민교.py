
# coding: utf-8

# 여기서는 Seaborn라이브러리에서 제공하는 데이터셋 2)중에서 타이타닉 데이터셋을 사용한다.

# In[39]:


import pandas as pd
import seaborn as sns


# In[40]:


titanic = sns.load_dataset('titanic')
titanic


# In[41]:


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


# In[42]:


# 2. 컬럼명 확인하기
print(titanic.columns)
print(len(titanic.columns))


# In[43]:


# 3. 각 컬럼별 유닉크한 값 구하기
titanic_col_List = titanic.columns
for i in titanic_col_List:
    print(f'{i}의 유니크 값 리스트 \n {titanic[i].unique()}')
    print('='*80)


# In[44]:


# 4. 나이에 대한 최소, 최대
print(f"타이타닉 탑승자 중 가장 나이가 많은 사람: {titanic['age'].max()}살")
print(f"타이타닉 탑승자 중 가장 나이가 어린 사람: {titanic['age'].min()}살")


# In[45]:


# 5. 성별 생존률의 개수
sex_Survived = titanic.groupby('sex')['survived']
print(sex_Survived.count())


# In[54]:


# 6. 남자, 여자 명수
titanic_sexList = titanic['sex']

Male_Cnt = titanic[titanic['sex']=="male"]
feMale_Cnt = titanic[titanic['sex']=="female"]
print(f"타이타닉 탑승자 중 여성의 수: {feMale_Cnt['sex'].count()}명")
print(f"타이타닉 탑승자 중 남성의 수: {Male_Cnt['sex'].count()}명")


