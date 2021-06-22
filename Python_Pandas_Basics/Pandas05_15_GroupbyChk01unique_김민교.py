
# coding: utf-8

# ## lifeExp 열을 연도별로 그룹화하여 평균 계산하기

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[3]:


print(df.head(n=10))


# In[4]:


print(df.groupby('year')['lifeExp'].mean())


# In[7]:


print(df['year'].unique())


# In[8]:


uniList = df['year'].unique()
uniListsu = df['year'].nunique()
print(type(uniList))
print(type(uniListsu))
print(uniListsu)
print(uniList, '\n================')

