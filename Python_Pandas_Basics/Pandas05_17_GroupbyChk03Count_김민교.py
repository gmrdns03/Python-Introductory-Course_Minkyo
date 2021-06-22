
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[5]:


print(df.groupby('continent')['year'].count())
print()
print()
print('='*20)
print(df.groupby('year')['lifeExp'].count())


# In[6]:


print(df['continent'].unique())


# In[14]:


uniList = df['continent'].unique()
for idx in uniList:
    print('>>>>>>>>> 1 >>>>>>>>> : ', idx, '\n')
    grContinent = df[df['continent'] == idx]
    print('>>>>>>>>> 2 >>>>>>>>> : ', len(grContinent),'\n\n', grContinent.head(3), '\n\n', '>>>>>>>>> 3 >>>>>>>>>:', '\n', grContinent.shape, end = "")
    print(grContinent['year'].count(), '\n\n')
    print('='*60)

