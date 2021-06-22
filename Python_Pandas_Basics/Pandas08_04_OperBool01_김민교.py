
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


scientists = pd.read_csv('./../data/scientists.csv')


# In[7]:


print(scientists.columns, '\n', scientists.shape)


# In[8]:


ages = scientists['Age']
print(ages.max())


# In[9]:


print(ages.mean())


# In[10]:


print(ages[ages > ages.mean()])


# In[11]:


print(ages > ages.mean())


# In[12]:


print(type(ages > ages.mean()))


# In[13]:


manual_bool_values = [True, True, False, False, True, True, False, True]
print(ages[manual_bool_values])

