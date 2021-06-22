
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


titanic = sns.load_dataset('titanic')


# In[3]:


titanic['survived'].unique()


# In[4]:


titanic['sex'].unique()


# In[5]:


# 5. 성별 생존률의 개수
sur_titanic = titanic[titanic['survived'] == 1]
sex_Survived = sur_titanic.groupby('sex')['survived']
print(sex_Survived.count())

