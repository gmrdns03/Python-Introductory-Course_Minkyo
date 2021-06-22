
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('./../data/gapminder.tsv', sep = '\t')

multi_Group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']]
print(multi_Group_var)

print(multi_Group_var.mean())
print('='*60)
print(multi_Group_var.mean().count())


# In[8]:


#검증하기
uniList_year = df["year"].unique()
uniList_continent = df["continent"].unique()
uniList_continent.sort()
print('='*60)

for i in uniList_year:
    print('='*60)
    Chk01 = df[df["year"] == i]
    for j in uniList_continent:
        Chk02 = Chk01[df["continent"] == j]
        print(f"{i}년 {j:^10}지역 기대수명 평균/GDP 평균: {Chk02['lifeExp'].mean():.2f} / {Chk02['gdpPercap'].mean():.2f}")
           
print(f"lifeExp Cnt : {len(uniList_year) * len(uniList_continent)}")
print(f"gdpPercap Cnt : {len(uniList_year) * len(uniList_continent)}")
        
    

