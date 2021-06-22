'''
[메서드의 또 다른 호출 방법]
	- 클래스를 통해 메서드를 호출하는 것도 가능
	- 클래스 이름.메서드 형태로 호출할 때는 객체 a를 첫 번째
		매개변수 self에 꼭 전달해주어야 한다.
	- 반면에 다음처럼 객체.메서드 형태로 호출할 때는 self를
		반드시 생략해서 호출해야 한다


[함수]
- 재사용을 하기위한 것
- 함수명()
- 매서드: 클래스 안에 들어가 있는 함수
		'''

class FourCal:
	def detdata(self, first, second):
		self.first = first
		self.second = second

a = FourCal()

FourCal.setdata(a, 2, 3)

print(a.first, a.second)
a.setdata(4, 5)
print(a.first, a.second)