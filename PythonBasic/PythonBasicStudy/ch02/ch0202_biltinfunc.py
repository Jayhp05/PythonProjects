# 파이썬 내장 함수

# 절대값을 반환하는 함수
print(abs(-10))

# 시퀀스(문자열, 튜플, 리스트)에서 최대값, 최솟값을 반환하는 함수
print(max([3, 6, 1, 7, 9]), min([3, 6, 1, 7, 9]), max("python"))

# pow(a, b) 함수는 a의 b승을 반환하는 함수
print(pow(2, 2))

# 입력 받은 ASCII 코드 값에 해당하는 문자를 반환하는 함수
print(chr(65), chr(66), chr(67), chr(97), chr(98), chr(99))

print(chr(0xAC00), chr(0xAC00 + 11171))

# 인수로 입력 받은 객체를 표현하는 문자열을 반환하는 함수
print(str(object), str(123), str([]), str(()), str(chr(65)))

# range([start,]stop[,step] ) 함수는 숫자 자료 start, stop, step을
# 입력 받아 그 범위에 해당하는 정수를 range 타입으로 반환하는 함수
# Python 2.7에서는 list 타입을 반환하였으나 Python 3에서는 순차적인
# 숫자 스트림을 반환함, 아래는 0 ~ 10-1까지의 숫자 스트림을 반환함
print(range(10))

# type() 함수는 인수로 지정한 객체의 자료형을 반환하는 함수
print(type(range(10)), str(range(10)))
print(range(1, 11, 1), range(1, 11, 2))

sum = 0
for i in range(1, 11, 1):
    sum += i
print(sum)

