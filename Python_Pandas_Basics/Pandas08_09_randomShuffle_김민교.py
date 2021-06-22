
# coding: utf-8

# In[3]:


import random

random.seed(10)
print(random.random())


# In[2]:


import random
import pandas as pd
scientists = pd.read_csv('./../data/scientists.csv')

random.seed(10)
random.shuffle(scientists['Age'])
print(scientists['Age'])

