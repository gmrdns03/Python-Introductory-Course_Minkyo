
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[3]:


uniList = df['year'].unique()
print(uniList)


# In[8]:


for idx in uniList:
    yearList = df[df['year']== idx]
    print(f"{idx}년도 POP의 평균: {yearList['pop'].mean():.2f}")

