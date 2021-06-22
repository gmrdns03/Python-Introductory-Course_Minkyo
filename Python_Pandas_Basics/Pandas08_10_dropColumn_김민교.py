
# coding: utf-8

# In[1]:


import pandas as pd
scientists = pd.read_csv('./../data/scientists.csv')


# In[2]:


scientists_dropped = scientists.drop(['Age'], axis=1)

print(scientists_dropped.columns)

