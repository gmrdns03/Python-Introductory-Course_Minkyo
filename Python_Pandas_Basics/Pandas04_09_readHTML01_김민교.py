
# coding: utf-8

# In[13]:


import pandas as pd


# In[31]:


url = './../_WSPython10/Test_01_HTML.html'

tables = pd.read_html(url)


# In[32]:


print(len(tables), '\n==>')

print(tables, '\n==>')

for i in range(len(tables)):
    print("tables[%s]"% i, '\n')
    print(tables[i], '\n')
    
df = tables[0]
print(df.columns, '\n')

