
# coding: utf-8

# 데이터 추출하기_ 슬라이싱 구문
# range 메서드 39쪽

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[3]:


df.head(3)


# In[4]:


subset = df.loc[:, ['year', 'pop']]
print(subset.head())


# In[5]:


subset = df.iloc[:, [2, 4, -1]]
print(subset.head())

