
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_csv("./../DataSet/read_csv_sample.csv")
print(df)
print(type(df))


# In[ ]:


file_path = "./../DataSet/read_csv_sample.csv"

df = pd.read_csv(file_path)
print(df)
print(type(df))

