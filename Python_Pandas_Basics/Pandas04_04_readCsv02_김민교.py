
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_csv("./../DataSet/read_csv_sample.csv")
print(df)
print(type(df))


# In[7]:


file_path = "./../DataSet/read_csv_sample.csv"

df = pd.read_csv(file_path)
print(df)
print(type(df))


# In[10]:


df = pd.read_csv(file_path)
print(df, '\n')

df2 = pd.read_csv(file_path, header = None)
print(df2, '\n')

df3 = pd.read_csv(file_path, index_col = None)
print(df3, '\n')

df4 = pd.read_csv(file_path, index_col = 'c0')
print(df4, '\n')

