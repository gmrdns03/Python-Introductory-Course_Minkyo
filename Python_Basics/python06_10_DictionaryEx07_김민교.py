#딕셔너리 안에 찾으려는 Key 값이 없을 경우 
# 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용하면 편리하다.

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('nokey', 'babo'))
print('-' *50)

# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)
