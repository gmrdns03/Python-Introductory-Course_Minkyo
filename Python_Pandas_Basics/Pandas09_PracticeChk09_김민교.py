
# coding: utf-8

# In[1]:


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


# In[2]:


# 문제7 sawonDB 데이터에서 전산부 직원의 평균연봉 출력
deptno30_sawonDB = df_sawonDB[df_sawonDB['deptno']== 30]
deptno30_Moneymean = deptno30_sawonDB['sapay'].mean()

print(f'전산부 직원의 평균 연봉은 : {deptno30_Moneymean:.2f}만원 입니다.')

