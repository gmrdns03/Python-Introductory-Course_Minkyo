

# a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려준다.
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.keys())
print('-' *50)
'''
dict_keys 객체는 다음과 같이 사용할 수 있다.
리스트를 사용하는 것과 차이가 없지만, 
리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.

dict_values 객체와 dict_items 객체 역시 dict_keys 객체와 마찬가지로 
리스트를 사용하는 것과 동일하게 사용할 수 있다.
'''
for k in a.keys():
	print(k)
print('-' *50)

# dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
vList = list(a.keys())
print(vList)
print('-' *50)


