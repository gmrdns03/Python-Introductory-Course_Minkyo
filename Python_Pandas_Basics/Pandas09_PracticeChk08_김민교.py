
# coding: utf-8

# In[7]:


import pandas as pd

df_depDB = pd.read_csv('./../data/deptDB.csv')
df_sawonDB = pd.read_csv('./../data/sawonDB.csv')
df_gogekDB = pd.read_csv('./../data/gogekDB.csv')


df_depDB.columns = ['deptno', 'dname', 'loc']
df_sawonDB.columns = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr']
df_gogekDB.columns = ['gobun', 'goname', 'gotel', 'gojumin', 'godam']

df_depDB = df_depDB.replace("'", " ", regex=True)
df_sawonDB = df_sawonDB.replace("'", " ", regex=True)
df_gogekDB = df_gogekDB.replace("'", " ", regex=True)

print(df_depDB)
print(df_sawonDB)
print(df_gogekDB)


# In[8]:


# 문제 1
sawon_1988 = df_sawonDB[df_sawonDB['sahire'].str.contains('1988')]
print(sawon_1988)


# In[9]:


# 문제 2
sawon_april = df_sawonDB[df_sawonDB['sahire'].str.contains('/04/')]
print(sawon_april)


# In[11]:


# 문제 3
slist = []
for i, value in enumerate(df_sawonDB['sabun']):
    if value %2 ==0:
        slist.append(i)
        
print(df_sawonDB.loc[slist])

