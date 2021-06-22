
# 일반적으로 다른 언어에서 자료를 교환할 때 쓰는 방법
vI01 = 20
vI02 = 30
print("교환전 값 : ", vI01, vI02)
temp = vI01
vI01 = vI02
vI02 = temp
print("교환후 값 : ", vI01, vI02)


# 파이썬에서 가능한 방법
a = 3
b = 5
print("교환전 값 : ", a, b)
a, b = b, a
print("교환후 값 : ", a, b)

