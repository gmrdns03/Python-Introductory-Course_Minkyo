
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd. DataFrame({
    'Name' :["Rosaline", 'William Gosset'],
    'Occupation' : ["Chemist", 'Statistician'],
    "Born" : ['1920-07-25', '1876-06-13'],
    'Died' : ['1958-04-16', '1937-10-16'],
    'Age':[37,61]
})
print(scientists)


# In[4]:


scientists = pd. DataFrame(
    data = {'Occupation' : ["Chemist", 'Statistician'],
    "Born" : ['1920-07-25', '1876-06-13'],
    'Died' : ['1958-04-16', '1937-10-16'],
    'Age':[37,61]},
    index = ["Rosaline", 'William Gosset'],
    columns = ['Occupation', "Born", 'Died', 'Age'])
print(scientists)


# In[5]:


from collections import OrderedDict


# In[7]:


scientists = pd.DataFrame([
    ('Name', ["Rosaline", 'William Gosset']),
    ('Occupation', ["Chemist", 'Statistician']),
    ("Born", ['1920-07-25', '1876-06-13']),
    ('Died', ['1958-04-16', '1937-10-16']),
    ('Age', [37,61])
])

print(scientists)
print(type(scientists[0]))


# In[9]:


scientists = pd.DataFrame(OrderedDict([
    ('Name', ["Rosaline", 'William Gosset']),
    ('Occupation', ["Chemist", 'Statistician']),
    ("Born", ['1920-07-25', '1876-06-13']),
    ('Died', ['1958-04-16', '1937-10-16']),
    ('Age', [37,61])
])
)
print(scientists)

