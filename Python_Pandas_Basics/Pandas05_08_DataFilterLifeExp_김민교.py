
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


s = pd.Series([4,2,0,8])
print(s)
print()
print(s.max())
print(s.min())
print(s.mean())


# In[9]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')

df.shape


# In[25]:


lifeExp_df = df['lifeExp']

print('최대 기대수명:\n', lifeExp_df.max(),'\n')
print('최소 기대수명:\n', lifeExp_df.min())


# In[20]:


dfL = df.loc[:, 'lifeExp']
print(dfL.shape)
print(dfL.max())
print(dfL.min())


# In[19]:


dfL = df.iloc[:, 3]
print(dfL.max())
print(dfL.min())

