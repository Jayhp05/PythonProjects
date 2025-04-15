############## 클래스 정의 ##############

# 클래스는 새로운 이름공간을 지원하는 단위이며 자료형 이다.
# 파이썬에서 이름공간을 구성하는 단위
# 모듈 : 파일 단위로 이름공간을 구성
# 클래스 : 클래스 영역 내에 이름공간을 구성
# 인스턴스 : 인스턴스 영역 내에 이름공간을 구성
# 클래스는 객체를 만들기 위한 설계도라 할 수 있으며
# 인스턴스는 클래스로 부터 만들어진 객체를 의미한다.
class Human:
    name = "홍길동"

# Human 클래스 이름공간에 새로운 age라는 이름을 생성
Human.age = 25
print(Human, " - ", Human.name, " - ", Human.age)
print(dir(Human))

# Human 클래스 이름공간에서 age 이름을 삭제
del(Human.age)
print(dir(Human))

# 인스턴스는 클래스와 독립적으로 이름공간을 가짐
# 파이썬은 동적으로 인스턴스 멤버를 추가할 수 있음
h = Human()
h.age = 30
print(h, " - ", h.name, " - ", h.age)

# 인스턴스는 생성될 때 마다 각각의 이름공간을 가짐
h2 = Human()
h2.age = 50
print(h2, " - ", h2.name, " - ", h2.age)

# 인스턴스 h2의 이름공간에 name이라는 이름을 생성
# 클래스의 이름공간과 인스턴스의 이름공간은 다름
h2.name = "이순신"
print(h2, " - ", h2.name, " - ", h2.age, " - ", Human.name)

# 몸체가 없는 클래스 정의 시에 pass를 사용함
class Animal:
    pass

# 동적으로 클래스 멤버를 추가할 수 있음
Animal.age = 10

# 인스턴스를 생성하고 동적으로 인스턴스 멤버를 추가할 수 있음
a = Animal()
a.kind = "고양이"
a.name = "야옹이"
a.age = 5
print(a.name, " - ", a.age, " - ", a.kind, " - ", Animal.age)