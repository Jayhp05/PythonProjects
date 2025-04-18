import keyword

# 파이썬 예약어와 예약어 개수를 출력
# len() 함수는 별도의 모듈 추가 없이 사용할 수 있는 내장함수
print(keyword.kwlist)
print(len(keyword.kwlist))

# 변수 생성 없이 바로 사용할 수 없음
# print(a)

# 변수에 값이 할당 될 때 변수가 생성됨
a = 100
print(a)

# 변수를 삭제한다.
# del a
# print(a)

# 등호(=)를 사용해 변수에 값을 할당할 수 있다.
a = 1; b = 10; a = a + 10
print(a, b)

# 변수를 삭제한다.
# del a
# print(a)

# 변수 c, d에 각각 10, 100을 할당
c, d = 10, 100
print(c, d)

# 변수 x, y, z에 1000을 할당
x = y = z = 1000
print(x, y, z)

# c = c + 100을 줄여서 표현 - 확장 할당이라고 함
# +=, -=, *=, /= 등의 확장 할당 연산자가 있음
c += 100

 # 파이썬에서 모든 데이터는 객체로 다루고 있으며 변수는 객체의
# 레퍼런스(참조)를 가지고 있다고 말함, 아래에서 x는 객체를 가리키는
# 이름(변수)으로 100이 저장된 객체의 레퍼런스를 가지고 있음
x = 100

 # 아래에서 a의 두 번째 값을 변경하면 b에 저장된 a의 값도 변경됨
# a와 b에 저장된 a는 같은 객체를 가리키고 있기 때문
a = [1, 2, 3]; b = ["A", "B", "C", a]
print(b)

a[1] = 100
print(b)