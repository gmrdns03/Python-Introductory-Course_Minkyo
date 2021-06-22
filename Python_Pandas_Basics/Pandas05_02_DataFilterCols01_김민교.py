
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')
df.shape


# In[7]:


df.head(3)


# In[9]:


country_df = df['country']

print(type(country_df)) # 한개의 열만 가져오면 시리즈로 추출


# In[10]:


print(country_df.head())


# In[11]:


print(country_df.tail())


# In[12]:


subset = df[['country', 'continent', 'year']]

print(type(subset)) # 두개 이상의 열을 가져오면 데이터프레임으로 추출


# In[13]:


print(subset.head())


# In[14]:


print(subset.tail())

