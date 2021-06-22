
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv('./../data/gapminder.tsv', '\t')
df


# In[5]:


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

