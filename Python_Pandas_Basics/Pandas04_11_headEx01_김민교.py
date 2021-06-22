
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion', 'monkey', 'parrot', 'shark', 'whale', 'zebra']})


# In[3]:


print(df)


# In[4]:


print(df.head())


# In[5]:


print(df.head(3))


# In[6]:


print(df.head(-3))

