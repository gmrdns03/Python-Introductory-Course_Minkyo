
# coding: utf-8

# In[1]:


import pandas as pd


# In[20]:


df = pd.read_csv('./../data/gapminder.tsv', '\t')
df


# In[16]:


print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[6]:


len(df)


# In[7]:


df.head()


# In[8]:


df[0:5]


# In[9]:


df.head(n=7)


# In[10]:


df.tail()


# In[12]:


df[len(df)-5 : len(df)+1]


# In[13]:


df.tail(n=7)


# In[29]:


# 데이터의 자료형을 확인
print(type(df))


# In[23]:


#데이터 프레임의 열 확인
print(df.columns)


# In[24]:


#데이터프레임의 행 확인
print(df.dtypes)


# In[25]:


#데이터 집합과 각 열들의 자료형을 자세히 확인
print(df.info())


# In[27]:


#shape에서는 (행, 열)크기를 알 수 있다.
print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[28]:


df.shape

