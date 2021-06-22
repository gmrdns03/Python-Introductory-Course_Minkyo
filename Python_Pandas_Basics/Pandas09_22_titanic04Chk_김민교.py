
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


titanic = sns.load_dataset('titanic')


# In[4]:


ages = list(range(0, 90, 10))

for i in ages:
    start = i
    end = i+10
    ageTemp = titanic[(titanic['age'] >= start) & (titanic['age'] < end) & (titanic['survived']==0)]
    ageTemp_live = titanic[(titanic['age'] >= start) & (titanic['age'] < end) & (titanic['survived']==1)]
    print(f"{start}부터 {end}까지 사망자 수: {ageTemp['survived'].count()}", '\n'
         f"{start}부터 {end}까지 생존자 수: {ageTemp_live['survived'].count()}")
    print('='*40)

