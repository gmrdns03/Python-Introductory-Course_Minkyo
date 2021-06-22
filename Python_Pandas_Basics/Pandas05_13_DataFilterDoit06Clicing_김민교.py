
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# range와 슬라이싱 비교하기

# In[5]:


subset = df.iloc[:, :3]
print(subset.head())


# In[4]:


subset = df.iloc[:, 0:6:2]
print(subset.head())


# loc, iloc 속성 자유자재로 이용하기

# In[6]:


df.head(3)


# In[7]:


print(df.iloc[[0,99,999], [0,3,5]])


# In[8]:


print(df.loc[[0,99,999], ['country', 'lifeExp', 'gdpPercap']])


# In[9]:


print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])


# In[10]:


print(df.iloc[10:13, [0,3,-1]])

