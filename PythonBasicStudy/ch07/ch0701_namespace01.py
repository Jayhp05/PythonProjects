############# 클래스와 객체 #############

############ 이름 공간 ############
# 변수 g, a는 전역변수
g = 50
a = 10

# 변수 a, x, h는 함수 안에서 정의되어 지역변수
# 함수 안의 a는 함수 내부에서 정의된 지역변수
def func1(x):
    h = x + 100
    a = h + x + g

    return a

print(func1(5))

# 아래의 a는 이 모듈에서 정의한 전역변수
# 함수 내부에서 a가 정의되어 값을 지정했지만 변수의 스코프가
# 다르기 때문에 전역 변수 a에는 영향을 미치지 않음
print(a)

# 변수 x, h는 함수 안에서 정의되어 지역변수
# 함수 내부에서 전역 변수를 직접 사용해야 할 경우 변수 앞에
# global 키워드를 사용하면 전역영역에서 변수를 찾는다.
# 함수 내부에서 global a로 전역변수를 사용하고 있기 때문에
# 함수가 실행된 후에 전역변수 a의 값은 함수의 반환 값과 같다.
def func2(x):
    global a
    h = x + 100
    a = h + x + g

    return a

print(func2(5))
print(a)

# 객체가 사용된 공간의 이름 목록을 출력
print(dir(a))
print(dir(func2))
print(dir(object))