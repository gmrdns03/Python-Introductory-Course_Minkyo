
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[4]:


multi_Group_var = df.groupby(['year', 'continent'])[['lifeExp', 'pop']]
print(multi_Group_var)

print(multi_Group_var.mean())
print('='*60)
print(multi_Group_var.mean().count())

