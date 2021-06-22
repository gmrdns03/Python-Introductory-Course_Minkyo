
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

df_sawonDB


# In[9]:


df_sawonDB['sajob'] = df_sawonDB['sajob'].str.strip()


# In[13]:


sajobChk = df_sawonDB[(df_sawonDB['sajob']=='대리') | (df_sawonDB['sajob']=='사원')]
sajobChk


# In[17]:


sajobChk.groupby(['sajob'])['sabun'].count()


# In[21]:


sajobChk.groupby(['sajob'])['sabun'].count()>=4


# In[25]:


(sajobChk.groupby(['sajob'])['sabun'].count()>=4).values


# In[26]:


sajobChk = df_sawonDB[:][(df_sawonDB['sajob']=='대리')|(df_sawonDB['sajob']=='사원')]
sajobCntChk = sajobChk.groupby(['sajob'])['sabun'].count() >= 4

sajobChkResult = sajobCntChk[sajobCntChk.values]

for i, value in enumerate(sajobChkResult.index) :
    cal = df_sawonDB[df_sawonDB['sajob']== value]
    print(cal.groupby('sajob')['sapay'].mean())

