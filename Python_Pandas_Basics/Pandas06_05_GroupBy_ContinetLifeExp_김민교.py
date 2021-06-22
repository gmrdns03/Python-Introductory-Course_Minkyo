
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[2]:


contList = df.groupby('continent')['lifeExp'].mean()
print(contList)

