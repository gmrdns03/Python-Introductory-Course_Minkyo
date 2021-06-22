
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


# In[9]:


multi_Group_var = df.groupby(['year', 'continent'])['lifeExp']
print(multi_Group_var)
print('='*60)

print(multi_Group_var.mean())
print('='*60)
print(multi_Group_var.mean().count())


# In[23]:


#검증하기
uniList_year = df["year"].unique()
uniList_continent = df["continent"].unique()
uniList_continent.sort()
print('='*60)
for i in uniList_year:
    Chk01 = df[df["year"] == i]
    for j in uniList_continent:
        Chk02 = Chk01[df["continent"] == j]
        print(f"{i}년 {j:^10}지역 기대수명 평균: {Chk02['lifeExp'].mean():.2f}")
    print('='*60)        

        
    

