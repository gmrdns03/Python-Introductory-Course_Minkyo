
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np

s = pd.Series(['1. Ant.   ', '2. Bee!\n', '3.Cat\t', np.nan])
s


# In[7]:


s.str.strip()


# In[8]:


s.str.strip('.') # 점(.)을 넣으면 공백도 제거되지 않느다는 것 확인


# In[9]:


s.str.strip('123.!? \n\t')


# In[10]:


s.str.lstrip('123.')


# In[11]:


s.str.rstrip('.!? \n\t')

