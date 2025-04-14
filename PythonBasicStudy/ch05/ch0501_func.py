############# 함수 정의 #############

# 함수의 정의는 def로 시작하고 콜로(:)으로 끝남
# 함수 몸체의 시작은 들여쓰기로 구분함
# 함수를 선언하면 메모리에 함수 객체가 생성되고
# 이 함수를 가리키는 레퍼런스가 생성됨
def add(a, b):
    return a + b

# 함수 호출
print(add(10, 2))
print(add((3, 4), (5, 6, 7)))
print(add([1, 2, 3], [5, 6, 7]))

# 함수의 레퍼런스를 다른 변수에 할당해 사용할 수 있음
f = add
print(f is add)
print(f(100, 200))

# 함수 몸체는 한 개 이상의 문장(statement)이 존재해야 함
# 아무런 내용이 없는 함수를 정의할 때는 pass 키워드를 사용함
# pass는 아무것도 수행하지 않고 지나가겠다는 의미이며 아무것도
# 하지 않는 함수, 모듈, 클래스 등을 만들어야 할 경우가 있는데
# 이때 pass를 사용함
def no_body():
    pass

# pass가 반환하는 값이 없으므로 None이 반환됨
print(no_body())

# return은 함수를 종료하고 호출한 곳으로 돌아가는 명령
# 아래와 같이 콤마(,)로 구분해 반환하면 튜플로 묶어서 반환함
def t_swap(a, b):
    return b, a
print(t_swap(10, 20))

# 함수 몸체에서 return을 생략하거나 return만 적을 경우
# 함수는 종료되지만 반환되는 값이 없기 때문에 None이 반환됨
def setNum(num):
    x = num
print(setNum(100))

# 함수를 호출할 때 인수의 이름을 지정해 값을 넘겨 줄 수 있음
# 인수의 이름을 지정하지 않을 경우 순서를 맞춰줘야 함
def divide(a, b):
    return a / b

print(divide(10, 5))
print(divide(b=10, a=5))

# 함수를 정의할 때 인수의 기본 값을 정의할 수 있음
# 기본 값이 있는 인수는 값을 전달하지 않으면 기본 값으로 실행됨
# 주의 - 기본 값을 지정한 인수 뒤에 기본 값이 없는 인수가 올 수 없음
def multiple(a, b=1):
    return a * b

print(multiple(10))
print(multiple(10, 2))

# 가변인수는 변수 앞에 "*"를 붙여 지정하며 데이터 타입은 튜플이다.
def str_sum(*strs):
    print(type(strs))
    L = []
    for item in strs:
        L.append(item)
    return L

print(str_sum("파이썬은", "쉽고", "재미있다."))