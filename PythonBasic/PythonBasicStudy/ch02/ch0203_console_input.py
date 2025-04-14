# input()은 콘솔 입력으로 부터 데이터를 입력 받는 함수
name = input("name : ")
print(name)

# int() 함수는 문자열을 정수로 변환하는 내장 함수
sum = int(input("1 + 2 = "))

if sum == 3:
    print("맞음")
else:
    print("틀림")

# 연속적으로 콘솔로 부터 입력 받을 수 있음
name = input("name : ")
age = input("age : ")
gender = input("gender : ")

print(name, "님은", age, "살 이며", gender + "이군요.")
print("{}님은 {}살이며 {}이군요".format(name, age, gender))