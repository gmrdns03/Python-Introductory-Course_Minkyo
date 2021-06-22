
# 다른 주소를 가리키도록 만들수는 없을까?

# 1. 슬라이싱을 이용
a = [1,2,3]
b = a[:]
a[1] = 4
print(a, '\t', b)

#2. copy라는 외부 모듈을 가져와서 이용
a = [1,2,3]
from copy import copy
b = copy(a)
a[1] = 4
print(a, '\t', b)
print(id(a))
print(id(b))