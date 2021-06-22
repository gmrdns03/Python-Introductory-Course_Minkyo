# key로 Value 얻기 (get)

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print('-' *50)


# a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고 할 경우 
# a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을 돌려준다는 차이가 있다.
# 여기에서 None은 "거짓"이라는 뜻이라고만 알아두자.
#딕셔너리 안에 찾으려는 Key 값이 없을 경우 
# 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용하면 편리하다.
print(a.get('nokey'))
print(a.get('nokey', 'babo'))
# print(a['nokey'])
print('-' *50)

# 디폴트 값...아무것도 넣지 않았을 때 나오게 하는 값