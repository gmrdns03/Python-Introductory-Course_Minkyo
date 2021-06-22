
# coding: utf-8

# In[1]:


import pandas as pd
# 시리즈 만들기

s = pd.Series(['banana', 42])
print(s)


# In[2]:


s = pd.Series(['Wes McKinney', 'Creator of Pandas'])
print(s)


# In[4]:


s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index = ['Person', 'Who'])
print(s)

