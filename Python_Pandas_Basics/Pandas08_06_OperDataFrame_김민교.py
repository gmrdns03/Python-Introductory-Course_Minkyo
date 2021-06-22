
# coding: utf-8

# ## 불린 추출과 브로드캐스팅(65쪽)

# In[2]:


import pandas as pd


# In[3]:


scientists = pd.read_csv('./../data/scientists.csv')


# In[4]:


print(scientists[scientists['Age'] > scientists['Age'].mean()])


# In[5]:


print(scientists.loc[[True, True, False, True]])


# In[6]:


print(scientists * 2)
# 문자열은 *2 하여 두번 연결되고
# 숫자열은 *2로 연산된다.

