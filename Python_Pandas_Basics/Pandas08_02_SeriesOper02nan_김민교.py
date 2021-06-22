
# coding: utf-8

# ### 결측치 연산 결과 확인하기

# In[1]:


# 라이브러리 불러오기
import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90})

print(student1)
print(student2)

# 인덱스 개수가 맞지 않으면 동일하지 않은 인덱스는 NaN으로 나온다.
# NaN은 Not a Number의 준말
addition       = student1 + student2
subtraction   = student1 - student2
multiplication = student1 * student2
division        = student1 / student2

# 사칙연산 결과를 데이터 프레임으로 합치기(시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result, "\n", type(result))
print(addition, "\n", subtraction, "\n", multiplication, "\n", division)


# ### 결측치 처리하기

# In[2]:


# 라이브러리 불러오기
import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90})

print(student1)
print(student2)

# 인덱스 개수가 맞지 않으면 동일하지 않은 인덱스는 NaN으로 나온다.
# NaN은 Not a Number의 준말
sr_add       = student1.add(student2, fill_value=0)
sr_sub   = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

# 사칙연산 결과를 데이터 프레임으로 합치기(시리즈 -> 데이터프레임)
result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                      index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result, "\n", type(result))
print(sr_add, "\n", sr_sub, "\n", sr_mul, "\n", sr_div)

