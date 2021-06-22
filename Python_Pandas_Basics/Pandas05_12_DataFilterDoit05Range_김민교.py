
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[3]:


small_range = list(range(5))
print(small_range)


# In[4]:


df.head(3)


# In[5]:


subset = df.iloc[:, small_range]
print(subset.head())


# In[6]:


small_range = list(range(3, 6))
print(small_range)


# In[7]:


subset = df.iloc[:, small_range]
print(subset.head())


# In[8]:


small_range = list(range(0,6,2))
subset = df.iloc[:, small_range]
print(subset.head())

