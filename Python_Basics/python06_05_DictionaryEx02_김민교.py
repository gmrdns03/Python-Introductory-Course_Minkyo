'''
**딕셔너리 쌍 추가하기
{1: 'a'} 딕셔너리에 a[2] = 'b'와 같이 입력하면 
딕셔너리 a에 Key와 Value가 각각 2와 'b'인 2 : 'b'라는 딕셔너리 쌍이 추가된다.

 del 함수를 사용해서 del a[key]처럼 입력하면 지정한 Key에 해당하는 {key : value} 쌍이 삭제된다.
'''

a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pay'
print(a)
print('-' *50)

del a[2] # <-- []안에 있는 것은 인덱스 값이 아니라 Key값을 말하는 것
print(a)
print('-' *50)