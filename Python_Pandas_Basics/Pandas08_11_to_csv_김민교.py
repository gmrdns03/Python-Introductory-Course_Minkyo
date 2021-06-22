
# coding: utf-8

# In[3]:


import pandas as pd
data = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ['A', 'A+', 'B'],
       'basic' : ['C', 'B', 'B+'],
       'c++' : ['B+', 'C', 'C+'],
       }


# 판다스 DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
df = pd.DataFrame(data)
df.set_index('name', inplace = True)
print(df)


# In[4]:


# to_csv()메소드를 사용하여 CSV 파일로 내보내기
# 파일명은 df_sample.csv로 저장
df.to_csv("./df_sample.csv")

