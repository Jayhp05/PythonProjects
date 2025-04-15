import sys

# 변수를 선언하고 10진수, 8진수, 16진수 정수를 할당
i = 15; octal = 0o15; hexa = 0x15
print(i, octal, hexa)
print(type(i), type(octal), type(hexa))

# 최대 정수 - Python 2.7에서는 sys.maxint
# Python 2에서는 int형 32bit, long형 64bit 크기 였지만
# Python 3에서는 long형은 없어지고 int형의 크기가 유연해 졌다.
# Python 3에서 int형은 64bit 보다 더 큰 값을 가질 수 있다.
print(sys.maxsize)

h = 1234567890123456789012345678901234567890
print(type(h), " : ", h * h)

# 변수를 선언하고 실수(float)를 할당
x = 3.5; y = 2.3e3; z = -0.5e3
print(x, y, z)
print(type(x), type(y), type(z))

# 나머지 연산
print(i% 2, " : ", 3.5 % 2)

# 부동소수점 나누기(실수)
print(i / 2, " : ", 3.5 / 2)

# 정수 나누기 -소수점 이하 버림
print(i // 2, " : ", 3.5 // 2)

# 지수 연산
print(i ** 2, " : ", 3.5 ** 2)

# divmod() 함수는 몫과 나머지를 튜플로 반환하는 함수
print(divmod(i, 2), " : ", divmod(3.5, 2))

# 형 변환 함수를 이용해 실수를 정수로 정수를 실수로 변환
print(int(45.6), " : ", float(100))

import math
# math 모듈은 수학적으로 정의된 상수와함수를 지원
print(math.pi, math.e, math.sqrt(2))