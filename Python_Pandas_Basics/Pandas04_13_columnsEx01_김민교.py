
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')
df.shape


# In[3]:


df.columns

