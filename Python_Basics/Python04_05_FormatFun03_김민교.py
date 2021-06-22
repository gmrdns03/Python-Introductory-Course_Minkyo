a = "{2:<10}".format('aa','bb','cc')
b = "{1:>10}".format('aa','bb','cc')
c = "{:^10}".format('aa','bb','cc')
d = "{:w^10}".format('aa','bb','cc')
# <는 좌정렬 / >는 우정렬 / ^는 가운데 정렬/ w^는 가운데 정렬 외 w표시
print(a)
print(b)
print(c)
print(d)

x = 34213421
y = 342.134216
e1 = "{1:0.4f} {0:,d}".format(x,y)
#   인덱스값 : 형태
e2 = '{:w^10.2f}'.format(y)
e3 = "{0:,d} {1:0.4f}".format(x,y)

j = '{{  and  }}'
print(j)

print(e1)
print(e2)
print(e3)