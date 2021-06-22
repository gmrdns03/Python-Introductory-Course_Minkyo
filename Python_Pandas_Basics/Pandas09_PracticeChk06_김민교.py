
# coding: utf-8

# In[1]:


import pandas as pd
# 시리즈이름.str.contains('a', case=False)
#시리즈 안에서 a를 불린 형식으로 찾아주는 메소드
#case=False를 하면 대소문자 구별하지 않는다.


# In[2]:


s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23'])
s1.str.contains('og')


# In[5]:


ind = pd.Index(['Mouse', 'dog', 'house and parrot', '23.0'])
ind.str.contains('23')


# In[6]:


s1.str.contains('oG', case=False)


# In[7]:


s1.str.contains('house|dog')


# In[8]:


s1.str.contains('\\d') 


# In[9]:


s2 = pd.Series(['40', '40.0', '41', '41.0', '35'])
s2.str.contains('.0')

