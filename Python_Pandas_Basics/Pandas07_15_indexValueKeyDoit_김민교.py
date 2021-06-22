
# coding: utf-8

# In[2]:


import pandas as pd

scientists = pd.DataFrame(data={'Occupation': ['Chemist', 'Satatistian'],
                               'Born': ['1920-07-25', '1876-06-13'],
                               'Died' : ['1958-04-16', '1937-10-16'],
                                'Age' : [37,61]},
                         index=['Rosaline Franklin', 'William Gosset'],
                         columns=['Occupation', 'Born', 'Died', 'Age'])
print(scientists)


# In[3]:


first_row = scientists.loc['William Gosset']
print(type(first_row))


# In[4]:


print(first_row)


# In[5]:


#1. 인덱스 속성 사용하기
print(first_row.index)


# In[6]:


#2. values속성 사용하기
print(first_row.values)


# In[7]:


# 3. keys매서드 사용하기
print(first_row.keys())


# In[8]:


#4. index속성 응용하기
print(first_row.index[0])


# In[9]:


# 5. keys 메서드와 index 속성 응용하기
print(first_row.keys()[0])


# In[10]:


# 6. 시리즈의 mean, min, max, std메서드 사용하기 56쪽
print(scientists, '\n\n')

ages = scientists['Age']
print(ages,'\n\n')

print(ages.mean(), '\n\n')

print(ages.min(), '\n\n')

print(ages.max(), '\n\n')

print(ages.std(),'\n\n')

