# 가독성을 위해 한 줄로 된 간단한 함수가 필요한 경우 유용함
# 람다 함수의 몸체에는 식만 기술 할 수 있음
f = lambda x, y: x + y
print(f(10, 20))

# lambda를 정의하고 바로 호출할 수 있음
print((lambda x, y: x * y)(100, 10))

# 인수가 기본 값을 가지거나 가변 인수도 가질 수 있음
f1 = lambda x, y=10: x + y
f2 = lambda x, *args: args
print(f1(10))
print(f2(10, 20, 30, 40, 50))

# 람다 함수를 사용하지 않은 경우
def f1(x):
    return x + x

def f2(x):
    return x + x + x

def list_func(func):
    return [func(i) for i in range(1, 11)]

# 함수도 파이썬 객체이기 때문에 인수로 지정할 수 있음
print(list_func(f1))
print(list_func(f2))
# 람다 함수를 이용해 함수의 인수로 지정
print(list_func(lambda x: x + x))
print(list_func(lambda x: x + x + x))

def f(x):
    return x + x
l = [10, 20, 30, 40, 50]

# map() 내장 함수는 두 번째 인수로 지정한 시퀀스 자료형의 각 요소에
# 대해 첫 번째 인수로 지정한 함수를 적용하여 그 결과를 같은 시퀀스
# 자료형으로 접근할 수 있는 map 타입의 객체를 반환한다.
result = map(f, l)
print([i for i in result], result)

# 람다 함수와 map 함수를 활용한 예
result = map(lambda x: x + x, l)
print([i for i in result])

result = map(lambda x: x ** 2, range(1, 11))
print([i for i in result])

result = map(lambda x: len(x), ["단어들의", "길이", "리스트를 구함"])
print([i for i in result])

# filter() 내장 함수는 두 번째 인수로 지정한 시퀀스 자료 형의 각 요소에
# 첫 번째 인수로 지정한 함수를 적용한 결과가 참인 요소만 추출해 동일
# 한 시퀀스 자료형으로 접근할 수 있는 filter 타입의 객체로 반환한다.
l = [1, 6, 3, 10, 5,  8, 9, 2, 4, 7]

result = filter(lambda x: x % 2 == 0, l)
print(list(result), result)

result = filter(lambda x: x > 5, l)
print(list(result))

from functools import reduce
#import functools

# 첫 번째 인수인 함수는 반드시 2개의 인수를 받아야 한다.
# 첫 번째 단계에서 초기 값 100이 x에 할당 되고 리스트의 1이
# y에 할당 된다. 두 번째 단계에서 x에 101이 할당되고 y에는
# 리스트의 2가 할당된다. 세 번째 단계에서 x에 103이 할당되고
# y에는 리스트의 3이 할당되어 결과는 106이 된다.
result = reduce(lambda x, y: x + y, [1, 2, 3], 100)
# result = functools.reduce(lambda x, y: x + y, [1, 2, 3], 100)
print(result)

# 1 ~ 10까지 합 구하기
# 첫 번째 단계의 초기 값이 생략되면 첫 번째 단계의 x는 0이 할당된다.
result = reduce(lambda x, y: x + y, range(1, 11))
print(result)

# 문자열 순서 뒤집기 -첫 번째 단계의 x에는 공백문자가 할당된다.
result = reduce(lambda x, y: y + x, "abcde")
print(result)