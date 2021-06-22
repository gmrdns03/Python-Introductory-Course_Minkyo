
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

df_sawonDB


# In[4]:


df_sawonDB['sajob'] = df_sawonDB['sajob'].str.strip()


# In[9]:


sajobChk = df_sawonDB[:][df_sawonDB['sajob'].isin(['대리', '사원'])]
sajobCntChk = sajobChk.groupby(['sajob'])['sabun'].count() >= 4

sajobChkResult = sajobCntChk[sajobCntChk.values]

for i, value in enumerate(sajobChkResult.index) :
    cal = df_sawonDB[df_sawonDB['sajob']== value]
    print(cal.groupby('sajob')['sapay'].mean())

