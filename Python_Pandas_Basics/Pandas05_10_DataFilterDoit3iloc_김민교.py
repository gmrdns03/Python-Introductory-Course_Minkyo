
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[3]:


print(df.head(3))


# In[4]:


print(df.iloc[1])


# In[5]:


print(df.iloc[99])


# In[6]:


print(df.iloc[-1])


# In[7]:


print(df.tail(1))
print(df.shape)
print(df.iloc[1703])


# In[8]:


print(df.iloc[[0, 99, 999]])

