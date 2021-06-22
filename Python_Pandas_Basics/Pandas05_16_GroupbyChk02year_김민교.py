
# coding: utf-8

# ## lifeExp 열을 연도별로 그룹화하여 평균 계산하기

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')


# In[3]:


print(df.head(n=10))


# In[21]:


# 각 년도에서 기대수명의 평균값을 구한 것이다.
print(df.groupby('year')['lifeExp'].mean())
print('='*20)


# In[7]:


print(df['year'].unique())


# In[8]:


uniList = df['year'].unique()
uniListsu = df['year'].nunique()
print(type(uniList))
print(type(uniListsu))
print(uniListsu)
print(uniList, '\n================')


# In[20]:


for idx in uniList:
    print('>>>>>>>>> 1 >>>>>>>>> : ', idx, '\n')
    grYear = df[df['year'] == idx]
    print('>>>>>>>>> 2 >>>>>>>>> : ', len(grYear),'\n\n', grYear.head(3), '\n\n', '>>>>>>>>> 3 >>>>>>>>>:', '\n\n', grYear.shape)
    print(grYear["lifeExp"].mean())
    

