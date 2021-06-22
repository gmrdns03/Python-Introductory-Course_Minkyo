
# coding: utf-8

# ## jason, excel로 저장하기
# 
# pandas.ExcelWriter
# https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html
# 
# pandas.DataFrame.to_excel
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
# 
# 하나 이상의 데이터프레임 파일을 다른 시트에 저장할 때에는 Container변수가 하나 필요하다.

# In[1]:


import pandas as pd
data = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ['A', 'A+', 'B'],
       'basic' : ['C', 'B', 'B+'],
       'c++' : ['B+', 'C', 'C+'],
       }

df = pd.DataFrame(data)
df.set_index('name', inplace = True)
print(df)

# to_json() 메소드를 사용하여 JSON파일로 내보내기
# 파일명은 df_sample.json으로 저장
df.to_json('./df_sample.json')


# In[2]:


import pandas as pd
data = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ['A', 'A+', 'B'],
       'basic' : ['C', 'B', 'B+'],
       'c++' : ['B+', 'C', 'C+'],
       }

df = pd.DataFrame(data)
df.set_index('name', inplace = True)
print(df)

# to_excel()메소드를 사용하여 엑셀 파일로 내보내기
# 파일명은 df_sample.xlsx로 저장
df.to_excel('./df_sample.xlsx')


# In[3]:


import pandas as pd
data = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ['A', 'A+', 'B'],
       'basic' : ['C', 'B', 'B+'],
       'c++' : ['B+', 'C', 'C+'],
       }

data2 = {'c0': [1,2,3],
        'c1': [4,5,6],
        'c2': [7,8,9],
        'c3': [10,11,12],
        'c4': [13,14,15]}

df = pd.DataFrame(data)
df.set_index('name', inplace = True)
print(df)

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace = True)
print(df2)

# df을 sheet1으로, df2를 cheet2로 저장
# 엑셀파일명은 'df_excelwriter.xlsx'
writer = pd.ExcelWriter('./df_excelwriter.xlsx')
df.to_excel(writer, sheet_name='시트1')
df2.to_excel(writer, sheet_name='시트2')
writer.save()

