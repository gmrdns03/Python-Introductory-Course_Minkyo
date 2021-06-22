
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
df


# In[4]:


df.groupby(['Animal']).mean()

