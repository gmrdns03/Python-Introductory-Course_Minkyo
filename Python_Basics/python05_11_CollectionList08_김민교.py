a= [1,2,3,1,2,3]
result01 = a.remove(3)
print(result01)
print(a)

print('-'*20)

a = [1,2,3,4]
result02 = a.pop()
print(result02)
print(a)
print('-'*20)

a= [1,2,3,1,2,3]
result03 = a.pop(a[0]) # -- > 왜 잘 안나옴?
print(result03)
print(a)
print('-'*20)