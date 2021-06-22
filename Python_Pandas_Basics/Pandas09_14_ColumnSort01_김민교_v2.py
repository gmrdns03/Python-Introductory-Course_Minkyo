
# coding: utf-8

# In[8]:


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

df_sawonDB


# In[4]:


columnsSort = df_sawonDB.columns.sort_values(ascending=True)
print(columnsSort)


# In[5]:


df_sawonDB[columnsSort]


# In[7]:


# 문제8 컬럼 이름순 재배치, sort_values()함수 적용
# ascending의 디폴트 값은 True(오름차순)으로 되어있다.
# axis=0이면 인덱스가 순서대로 바뀌고, axis=1이면 컬럼이 순서대로 바뀐다.
df_sawonDB_sort = df_sawonDB.sort_index(axis=1,ascending=True)
df_sawonDB_sort

