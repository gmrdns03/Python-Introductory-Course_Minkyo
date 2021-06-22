
# coding: utf-8

# 1번 1988년에 입사한 레코드 출력
# 2번 4월에 입사한 레코드 출력
# 3번 사원번호 짝수 레코드만 출력
# 4번 직위별 연봉 평균
# 5번 직위, 성별 별 연봉 평균

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


# In[13]:


print(df_sawonDB['sahire'])


# In[51]:


# 1번 1988년에 입사한 레코드 출력
yearData = df_sawonDB['sahire']
print(type(yearData[0]))
print(int(yearData[0][:6]))
for i in range(len(yearData)):
    if int(yearData[i][:6]) == 1988:
        print(f"태어난 년도가 {yearData[i][:6]:>5}년인 사원의 데이터 ↓↓↓")
        print(df_sawonDB.iloc[i])
        print('='*60)
    else: pass
    


# In[50]:


# 2번 4월에 입사한 레코드 출력
yearData = df_sawonDB['sahire']
# print(type(yearData[0]))  --> class 'str'>
# print(int(yearData[0][7:9])) --> 11
for i in range(len(yearData)):
    if int(yearData[i][7:9]) == 4:
        print(f"태어난 달이 {yearData[i][7:9]:>5}월인 사원의 데이터 ↓↓↓")
        print(df_sawonDB.iloc[i])
        print('='*60)
    else: pass


# In[55]:


# 3번 사원번호 짝수 레코드만 출력
sabun_sawonDB = df_sawonDB['sabun']
# print(sabun_sawonDB)
# print(type(sabun_sawonDB[0])) --> <class 'numpy.int64'>
for i in range(len(sabun_sawonDB)):
    if sabun_sawonDB[i] %2 ==0:
        print(f"사번이 {sabun_sawonDB[i]:>5}번인 사원의 데이터↓↓↓")
        print(df_sawonDB.iloc[i])
        print('='*60)
    else: pass


# In[53]:


# 4번 직위별 연봉 평균
sajob_Moneymean = df_sawonDB.groupby('sajob')['sapay'].mean()
print(sajob_Moneymean)


# In[54]:


# 5번 직위, 성별 별 연봉 평균
sajobsex_Moneymean = df_sawonDB.groupby(['sajob', 'sasex'])['sapay'].mean()
print(sajobsex_Moneymean)

