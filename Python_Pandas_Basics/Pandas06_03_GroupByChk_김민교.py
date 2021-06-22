
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[2]:


type(df)


# In[3]:


type(df['pop'])


# In[4]:


grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df["pop"])


# In[5]:


grouped_year_df["pop"].mean()

