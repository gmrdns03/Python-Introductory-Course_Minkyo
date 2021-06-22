
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv('./../data/gapminder.tsv', sep='\t')


# In[4]:


df.head(3)


# In[5]:


df.shape


# In[6]:


df.tail(3)


# In[7]:


loc00 = df.loc[0]


# In[8]:


print(loc00)
print(type(loc00))


# In[9]:


df.loc[90:100]


# In[10]:


print(df.loc[99])


# In[11]:


print(df.loc[-1])


# In[12]:


df.iloc[-1]


# In[13]:


len(df)

