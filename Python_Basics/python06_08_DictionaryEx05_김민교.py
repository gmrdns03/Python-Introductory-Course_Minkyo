
# Value 리스트 만들기(values)
# Key를 얻는 것과 마찬가지 방법으로 Value만 얻고 싶다면 values 함수를 사용하면 된다.
# values 함수를 호출하면 dict_values 객체를 돌려준다.
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.values())
print('-' *50)

# Key, Value 쌍 얻기(items)
print(a.items())
iList = list(a.items())
print(iList)
print('-' *50)

# Key: Value 쌍 모두 지우기(clear)
#clear 함수는 딕셔너리 안의 모든 요소를 삭제한다. 
# 빈 리스트를 [ ], 빈 튜플을 ( )로 표현하는 것과 마찬가지로 빈 딕셔너리도 { }로 표현한다.
a.clear()
print(a)