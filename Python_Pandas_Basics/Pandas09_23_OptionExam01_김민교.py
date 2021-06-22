
# coding: utf-8

# In[2]:


import pandas as pd

deptDB = pd.read_csv('./../data/deptDB.csv')
sawonDB = pd.read_csv('./../data/sawonDB.csv')
gogekDB = pd.read_csv('./../data/gogekDB.csv')

deptDB.columns = ['deptno', 'dname', 'loc']
sawonDB.columns = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr']
gogekDB.columns = ['gobun', 'goname', 'gotel', 'gojumin', 'godam']

deptDB = deptDB.replace("'", " ", regex = True)
sawonDB = sawonDB.replace("'", " ", regex = True)
gogekDB = gogekDB.replace("'", " ", regex = True)

for i in ['dname', 'loc']: 
    deptDB[i] = deptDB[i].str.strip()
    
for j in  ['saname', 'sajob', 'sahire', 'sasex']: 
    sawonDB[j] = sawonDB[j].str.strip()
    
gogekDB['goname'] = gogekDB['goname'].str.strip()

deptDB


# In[3]:


sawonDB


# In[4]:


gogekDB


# In[7]:


# 문제 12] 부서번호가 10, 20인 사원들의 이름과 월급과 부서번호를 출력하시오
deptno_1020 = sawonDB[(sawonDB['deptno']==10)|(sawonDB['deptno']==20)]

deptno_1020[['saname', 'sapay', 'deptno']]


# In[8]:


# 문제13] 급여가 1000~3000 사이의 직원 이름과 급여를 출력
sawonTemp = sawonDB[(sawonDB['sapay']>= 1000) |                    (sawonDB['sapay']<3000)]
sawonTemp[['saname', 'sapay']]


# In[10]:


# 문제21] 직업을 물어보게 하고 직업을 입력하면 해당 직업인 사원들의
# 이름과 직업이 출력되게 하는데, 없는 직업을 입력하면 '해당 직업은 없습니다' 라는 메시지가 출력되게 하시오.
jikup = input('직업 이름을 입력해주세요: ')
jikup_List = sawonDB['sajob'].unique()

if jikup in jikup_List:
    print(sawonDB[sawonDB['sajob'] == jikup][['saname', 'sajob']])

else: print('해당하는 직업은 존재하지 않습니다.')


