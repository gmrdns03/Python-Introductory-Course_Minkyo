
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


int_values = [1, 2, 3, 4, 5]
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
df = pd.DataFrame({"int_col": int_values, "text_col": text_values,
                  "float_col": float_values})
df


# In[3]:


df.info(verbose=False)


# In[4]:


df.dtypes


# In[5]:


df.info


# In[6]:


df.info()


# In[7]:


df.info(verbose=True)

