
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[2]:


print(df.groupby('continent')['year'].nunique(),"\n=========")
print(df.groupby('continent')['year'].unique(), "\n=========")
print(df.groupby('continent')['year'].unique()['Africa'], "\n=========")

