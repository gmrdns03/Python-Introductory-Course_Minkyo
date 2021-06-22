
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

print(df_depDB)
print(df_sawonDB)
print(df_gogekDB)


# In[7]:


# 문제6 인상급여 sawonDB 데이터에서 급여 10%인상한 필드 인상급여필드 생성
sapay01 = df_sawonDB['sapay']
sapay02 = sapay01 * 1.1
df_sawonDB['next_sapay'] = sapay02
print(df_sawonDB)


# In[13]:


# 문제7 sawonDB 데이터에서 전산부 직원의 평균연봉 출력
deptno30_sawonDB = df_sawonDB[df_sawonDB['deptno']== 30]
# print(deptno30_sawonDB)

deptno30_Moneymean = deptno30_sawonDB['sapay'].mean()
print(f'전산부 직원의 평균 연봉은 : {deptno30_Moneymean:.2f}만원 입니다.')


# In[19]:


# 문제8 컬럼 이름순 재배치, sort_values()함수 적용
# ascending의 디폴트 값은 True(오름차순)으로 되어있다.
# axis=0이면 인덱스가 순서대로 바뀌고, axis=1이면 컬럼이 순서대로 바뀐다.
df_sawonDB_sort = df_sawonDB.sort_index(axis=1,ascending=True)
print(df_sawonDB_sort)


# In[64]:


# 문제9 sawonDB데이터에서 직위가 사원과 대리 중 직원수가 4인 이상인 직위, 평균급여 출력
sawon_Cnt = df_sawonDB['sajob']
uniSawonDB = df_sawonDB['sajob'].unique()


for j in uniSawonDB:
    Cnt = df_sawonDB[df_sawonDB['sajob'] == j]
    Cnt2 = Cnt['sajob'].count()
    if Cnt2 >= 4:
        sapay_mean = Cnt.groupby('sajob')['sapay'].mean()
        print(f'직원 수가 4인 이상인 직위 {j}의 평균 급여는 {sapay_mean[0]:,}원 입니다.')
    else: pass
    
'''
for i in range(len(sawon_Cnt)):
    print(f'"{sawon_Cnt[i]}"')
    
uniSawonDB = df_sawonDB['sajob'].unique()

sawon_Cnt = df_sawonDB[df_sawonDB['sajob'] == "  사원 "]
deari_Cnt = df_sawonDB[df_sawonDB['sajob'] == "  대리 "]
print(sawon_Cnt['sajob'].count())
print(deari_Cnt['sajob'].count())
print(uniSawonDB)

a = df_sawonDB.groupby('sajob')['sapay'].mean()
print(a)
'''

