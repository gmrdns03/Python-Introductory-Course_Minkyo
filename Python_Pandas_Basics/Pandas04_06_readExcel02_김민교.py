
# coding: utf-8

# In[18]:


import pandas as pd
file_pathExcel = "./../DataSet/datalabPractice01.xlsx"


# In[19]:


dfExcel = pd.read_excel(file_pathExcel)
print(dfExcel)


# In[30]:


import pandas as pd
file_pathExcel = "./../DataSet/datalabPractice01.xlsx"
dfExcel2 = pd.read_excel(file_pathExcel,                          sheet_name="Sheet1", usecols=[0,1],                          skiprows=[0,2], skipfooter=1, header=None)
print(dfExcel2)

