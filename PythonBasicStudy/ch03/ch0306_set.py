# set은 수학에서 집합을 의미하며 프로그래밍에서도
# 수학에서 말하는 데이터의 집합을 구현하기 위해 사용한다.
# set은 사전 데이터 구조에서 값은 없고 키만 있는 데이터라 할 수 있다.
# set 생성 - 아래에서 중복된 값은 저장되지 않는다.
set1 = {0, 2, 4, 1, 4, 3}
print(set1)

# {}로 빈 사전을 생성하고 set() 함수로 빈 셋을 생성한다.
d = {}; s = set()
print(d, s)

# 반복문 안에서 한 줄에 출력
for i in set1:
    print(i, end="")\

# list를 set 데이터로 변환 - 중복 데이터 제거
l = ["영어", "수학", "과학", "수학", "영어"]
set2 = set(l)
print(set2)

# tupple을 set 데이터로 변환 - 중복 데이터 제거
t = ("Python", "Java", "Html", "Python")
set(t)

# dictionary를 set 데이터로 변환 - 키만 추출
d = {"영어": 80, "수학": 85, "과학": 82}
set(d)

# 중복된 문자를 제거하고 리스트로 변환
list(set("stop  stop stop stopstop"))

# in 연산자를 이용해 set의 값 멤버십 테스트
s = set({"영어", "수학", "국어"})
print("영어" in s, " - ", "과학" in s)

# list를 set 데이터로 변환 - 중복 데이터 제거
l = ["영어", "수학", "과학", "수학", "영어"]
set(l)

# tupple을 set 데이터로 변환 - 중복 데이터 제거
t = ("Python", "Java", "Html", "Python")
set(t)

# dictionary를 set 데이터로 변환 - 키만 추출
d = {"영어": 80, "수학": 85, "과학": 82}
set(d)

# 중복된 문자를 제거하고 리스트로 변환
list(set("stop  stop stop stopstop"))

# in 연산자를 이용해 set의 값 멤버십 테스트
s = set({"영어", "수학", "국어"})
print("영어" in s, " - ", "과학" in s)