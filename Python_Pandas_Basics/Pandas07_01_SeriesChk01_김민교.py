
# coding: utf-8

# In[1]:


# pandas 불러오기
import pandas as pd

dict_data = {'a': [1,3], 'b': [2,3], 'c': [3,3]}

# 판다스 Series() 함수로 딕셔너리 (dict_data)를 시리즈로 변환.
sr = pd.Series(dict_data)

# 변수 sr의 자료형 출력
print(type(sr))
print('\n')

# 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr)


# In[3]:


#02 Series index.py
# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2021-05-19', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr, '\n')

# 인덱스 배열을 변수 idx에 저장, 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print("sr.index:", idx, '\n')
print("sr.index type: ", type(idx), '\n')
print("sr.values :", val)
print("sr.values type : ", type(val))


# In[4]:


# series_element01
# 튜플을 시리즈로 변환(index 옵션에 인데스 이름 지정)
tup_data = ('영인', '2010-05-01', '여', True)

sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
print(sr, '\n')

# 원소를 1개 선택
print(sr[0], '\n')
print(sr['이름'])


# In[5]:


#Series_element2
# 여러개의 원소를 선택(인덱스 리스트 활용)
print(sr[[1,2]], '\n')
print(sr[['생년월일', '성별']], '\n')

#여러개의 원소를 선택(인덱스 범위 지정)
print(sr[1:2], '\n')
print(sr['생년월일':'성별'])


# In[6]:


a = range(1,7)
print(a)

for idx in a:
    print(idx)


# In[7]:


test = sr['생년월일' : '성별']
print(test)
type(test)

