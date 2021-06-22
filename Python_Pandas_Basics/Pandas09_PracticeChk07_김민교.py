
# coding: utf-8

# In[1]:


Animal = ['오렌지', '장미', '바다', '여우']

for idx in Animal:
    print(idx)

    
# aa는 인덱스 값을, bb는 요솟값을 반환해준다
# enumerate(Animal, 2)라고 하게 되면 인덱스값을 2 부터 표시한다.
for aa, bb in enumerate(Animal):
    print(aa, bb)


# In[ ]:




