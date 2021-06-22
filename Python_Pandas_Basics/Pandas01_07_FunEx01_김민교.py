
# coding: utf-8

# ### 기본함수 선언 연습01
# <h1> 기본 연습 </h1> 
# HTML : Hiper Text Markup Language
#             < , > , / 같은 것을 사용한다.
#             <h1>헤드 테그
#             </h1>막아준다

# In[2]:


def add(a, b):  #a, b는 매개변수
    return a + b

a = 3
b = 4
c = add(a, b)  # 3, 4는 인수

print("%d + %d =: %d"%(a, b, c))


# In[5]:


# 1. 일반적인 함수
def add(a, b): # a, b는 매개변수
    return a, b, a+b

a, b, result = add(b=5, a=3)
print("%d + %d = %d"%(b, a, result))


# In[6]:


#2. 입력값이 없는 함수
def say():
    return 'HI'

print(say())
print("_"*20)


# In[8]:


#3. 결괏값이 없는 함수
# 결괏값은 오직 return명령어로만 돌려받을 수 있다.

def add2(a, b):
    print('%d, %d의 합은 %입니다.'%(a, b, a+b))
    
print(add2(3,4))
print("_"*20)


# In[9]:


def say2():
    print('hi')
    
say2()
print("_"*20)

