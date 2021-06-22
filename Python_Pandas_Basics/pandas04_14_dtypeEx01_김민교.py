
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.DataFrame({'float': [1.0],
                   'int': [1],
                   'datetime': [pd.Timestamp('20180310')],
                   'string': ['foo']})
print(df)
print(df.dtypes)
print(type(df))

