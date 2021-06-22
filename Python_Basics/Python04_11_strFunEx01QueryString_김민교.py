'''
https://search.naver.com/search.naver? <<--'?'를 중심으로 해서 앞단이 URL
where=nexearch& <<--&는 QueryString
sm=top_hty&
fbm=1&
ie=utf8&
query=python

QueryString 개수 : 5개

'''

u = str(input("Url을 입력해주세요. : "))
s = u.split('&')
print(s)


c = len(s)
print('QueryString 개수 : ', c)


"""
u = str(input("Url을 입력해주세요. : "))
 for i in u:
	 if s = i.split(''):
		 print4
"""