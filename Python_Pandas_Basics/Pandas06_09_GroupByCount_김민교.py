
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[2]:


print(df.groupby('continent')['country'])


# In[3]:


print(df.groupby('continent')['country'].nunique())
print('='*60)
print(df.groupby('continent')['country'].unique())
print('='*60)
print(df.groupby('continent')['country'].unique()['Oceania'])
print('='*60)
print(df.groupby('continent')['country'].count())
print('='*60)
print(df.groupby('continent')['country'].count()['Africa'])

