
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


s = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama', 'hippo'], name='animal')
s


# In[3]:


s.isin(['cow', 'lama'])

