
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
df


# In[3]:


df.loc['viper']  # ==df.iloc[0]


# In[4]:


df.loc[0] # loc는 라벨명으로 값을 가져온다. 때문에 오류


# In[5]:


df.loc[['veper', 'sidewinder']]


# In[6]:


df.loc['cobra', 'shield']


# In[7]:


df.loc['cobra':'viper', 'max_speed']


# In[8]:


df.loc[[False, False, True]]


# In[9]:


df.loc[df['shield']>6]


# In[10]:


df.loc[df['shield'] >6, ['max_speed']]

