
# coding: utf-8

# ### **(두개)는 딕셔너리로 만들어진다
# #### Key = value형태의 결괏값이 그 딕셔너리에 저장된다.

# In[1]:


def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)
print_kwargs(name='foo', age = '3')

