
# coding: utf-8

# ## pandas.to_datetime
# https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
# 
# datetiem 형식으로 컨버트 되면 날짜 연산이 가능해진다.

# In[1]:


import pandas as pd

scientists = pd.read_csv('./../data/scientists.csv')


# In[2]:


print(scientists['Born'].dtype)
print(scientists['Died'].dtype)


# In[5]:


born_datetime = pd.to_datetime(scientists['Born'], format= '%Y-%m-%d')
print(born_datetime)
# 연도 포멧 형식에서 연도가 4자리인 경우 Y는 대문자로 써야 한다.
# 연도가 2자리인 경우 소문자 y를 쓴다.


# In[8]:


died_datetime = pd.to_datetime(scientists['Died'], format= '%Y-%m-%d')
print(died_datetime)


# In[10]:


died_datetime2 = died_datetime - born_datetime
print(died_datetime2)


# In[11]:


scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print(scientists.head())


# In[12]:


print(scientists.shape)


# In[13]:


scientists['age_days_dt'] = (scientists['died_dt']-scientists['born_dt'])
print(scientists)

