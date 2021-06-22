
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
df = pd.DataFrame(mydict)
df


# In[3]:


type(df.iloc[0])


# In[4]:


df.iloc[0]


# In[5]:


df.iloc[[0]]


# In[6]:


type(df.iloc[[0]])


# In[7]:


df.iloc[[0,1]]


# In[8]:


df.iloc[:3]


# In[9]:


df.iloc[[True, False, True]]


# In[10]:


df.iloc[0,1]


# In[11]:


df.iloc[[0,2], [1,3]]


# In[12]:


df.iloc[1:3, 0:3]


# In[14]:


df.iloc[:, [True, False, True, False]]

