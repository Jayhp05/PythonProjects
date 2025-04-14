########### 관계연산자 - 비교 연산자 ###########
# 두 피 연산자의 크기를 비교해 True 또는 False 값을 반환
print(5 > 10, " - ", 5 < 10)

# 문자열, 튜플, 리스트는 사전적인 순서로 대소 비교가 가능함
print("abcd" > "bac", " - ", "abcd" < "bac")
print((1, 5, 9) > (3, 4, 5), " - ", (1, 5, 9) < (3, 4, 5))
print([3, 2, 1] > [1, 5, 9], " - ", [3, 2, 1] < [1, 5, 9])
print("abc" == "bbc", " - ", (2, 3, 1) == (2, 3, 1))

########### 논리 연산자 ###########
# 진리(True 또는 False) 값을 피 연산자로 하여 논리적으로 비교해
# 진리 값을 반환하는 연산자

# 두 피연산자가 진리(True 또는 False) 값이어야 논리적 비교가 가능
print(1 > 2 or 1 < 2)
print(1 > 2 and 1 < 2)

# None, 0, 0.0, "", [], (), {}은 논리 연산에서 False 값을 가짐
print(not None, " - ", not 0, " - ", not "", " - ", not [])

# 진리 값은 사칙연산에서 True = 1, False = 0의 값을 가짐
print(True + 1, " - ", False + 1)
print(True * 10, " - ", False * 10)

############ 객체 판별 ############

# type() 함수는 객체의 타입(자료 형)을 반환하는 함수
print(type(100), type(100.0), type("타입"))
print(type([]), type(()), type({}))

a = 100;  b = 100.0; c = "타입";
l = [a, c]; t = (b, c); d = {"a": a, "c": c}

# None 객체는 아무 값도 아니다(또는 아무것도 없다)를 나타내는 객체
n = None
print(type(a) == type(0))
print(type(b) == type(0))
print(type(c) == type(""))
print(type(l) == type({}))
print(type(t) == type(()))
print(type(n) == type(None))

# id() 함수는 인터프리터가 관리하는 객체의 식별자를 반환
# is 연산자는 두 객체의 식별자가 동일한지 비교
l2 = l
print(id(l), " - ", id(l2))
print(l is l2)

# 숫자 리터럴은 변하지 않는 상수로 동일한 숫자는 새로 생성하지 않음
x = 1
y = 1
print(id(x), " - ", id(y))
print(x is y)

# 문자열 리터럴도 상수이므로 동일한 문자열은 새로 생성하지 않음
str1 = "타입"
str2 = "타입"
print(id(str1), " - ", id(str2))
print(str1 is str2)

# 아래는 각각 새로 생성되는 객체
l = ["a", "b", "c"]
l2 = ["a", "b", "c"]
print(id(l), " - ", id(l2))

# is 연산자는 두 객체의 식별자가 동일한지 체크하고
# == 연산자는 두 객체의 내용이 동일한지를 체크함
print(l is l2)
print(l == l2)