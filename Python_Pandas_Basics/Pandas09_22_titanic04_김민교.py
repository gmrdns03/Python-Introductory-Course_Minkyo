
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


titanic = sns.load_dataset('titanic')


# In[6]:


ages = list(range(0, 90, 10))

for i in ages:
    start = i
    end = i+10
    ageTemp = titanic[(titanic['age'] >= start) & (titanic['age'] < end)]
    ageTemp02 = ageTemp[ageTemp['survived'] ==0]
    print(f"{start}부터 {end}까지 사망자 수: {ageTemp02['survived'].count()}")

