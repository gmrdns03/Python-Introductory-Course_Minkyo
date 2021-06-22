
# coding: utf-8

# ## 벡터와 스칼라로 브로드캐스팅 수행하기(61쪽)

# In[4]:


import pandas as pd


# In[3]:


scientists = pd.read_csv('./../data/scientists.csv')

ages = scientists['Age']


# In[5]:


print(ages + ages)


# In[6]:


print(ages * ages)


# In[7]:


print(ages + 100)


# In[8]:


print(ages * 100)


# In[9]:


print(pd.Series([1,100]))


# In[10]:


print(ages, "\n\n")

print(pd.Series([1,100]), "\n\n")

print(ages + pd.Series([1,100]))


# In[11]:


print(ages)


# In[12]:


rev_ages = ages.sort_index(ascending=False)
print(rev_ages)


# In[13]:


print(ages*2)


# In[14]:


print(ages + rev_ages)

