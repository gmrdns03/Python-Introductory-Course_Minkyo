# 왼쪽, 오른쪽, 양쪽 공백지우기 ( lstrip/rstrip/strip)

a = '           hi          '

print(a)
print(a.lstrip()+"Chk")
# 문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다. 
print(a.rstrip()+"Chk")
#문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다.
print(a.strip()+"Chk")
# 문자열 양쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다.
print("-"*20)


#문자열 바꾸기(replace)
d = 'Life is too short'
print(d)
cng = d.replace('Life', 'Your leg')
print(cng)

print("-"*20)


