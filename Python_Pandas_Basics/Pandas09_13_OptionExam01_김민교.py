
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

print(df_sawonDB)


# In[13]:


# 문제10
df_sawonDB['saname'] = df_sawonDB['saname'].str.strip()
saName = input()

a = df_sawonDB[df_sawonDB['saname'] == saName]
pay = int(a['sapay']/12)
print(f'{saName}의 월급: {pay:.2f}')


# In[15]:


# 문제11
df_sawonDB['saname'] = df_sawonDB['saname'].str.strip()
saName = input()

b = df_sawonDB[df_sawonDB['saname'] == saName]
pay = int(b['sapay'])
if pay >= 3000: print('상위소득자입니다.')
elif 2000<= pay <3000: print('중위소득자입니다.')
else: print('월급 조정 대상자입니다.')

