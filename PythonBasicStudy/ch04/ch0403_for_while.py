# for 문은 다음과 같은 구조를 가지는 반복문 이다.
# for <반복용 변수> in <컨테이너 객체>:
#     반복 처리할 문장
# else:
#     for문이 정상적으로 모두 실행되었을 때 수행할 문장
#     break에 의해 종료되었을 때 수행되지 않음

# range() 함수를 이용한 for 문
for i in range(10):
    print(i)

# range() 함수를 이용해 1 ~ 10까지 합계 구하기
sum10 = 0
for i in range(1, 11):
    sum10 += i

print("1~10 합 : ", sum10)

# 리스트를 이용한 for 문
# 컨테이너에 빈 리스트를 지정할 수 있음
for i in []:
    print(i)
else:
    print("컨테이너 비어 있음")

# 컨테이너에 비어있지 않은 리스트 지정
for i in [1, 3, 5, 7, 9] :
    print(i, end=", ")

# 튜플을 이용한 for 문
sum10 = 0
t = tuple(range(1, 11))

for i in t:
    sum10 += i

print("1~10 합 : ", sum10)

# 사전을 이용한 for 문
ramen = {"농심라면": 2503, "삼양라면": 1750, "오뚜기라면": 765}

for key in ramen:
    print(key, " : ", ramen.get(key))

# 사전의 items() 메서드는 튜플의 리스트를 반환
books = {"Java": 25000, "Python": 24500, "Spring": 27000}
for book in books.items():
    print("{}의 가격은 {} 입니다.".format(book[0], book[1]))

# index 대신에 *를 이용하면 더 간결해 지는데 book은 튜플 데이터로
# *book은 튜플에 들어있는 2개의 데이터를 차례로 지정한 것과 같다.
for book in books.items():
    print("{}의 가격은 {} 입니다.".format(*book))

############## for 문 – zip() 함수 ##############

# zip() 함수를 이용한 반복문 - zip() 함수는 두 개의
# 시퀀스형 자료를 순서대로 한 쌍의 튜플로 만들어 주는 함수
# ('월요일', 'Mon'), ('화요일', 'Tue'), ('수요일', 'Wed'),...
e_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
h_days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
print(list(zip(h_days, e_days)))
print(dict(zip(h_days, e_days)))

# 두 시퀀스 자료형을 zip() 함수로 묶어서 반복문으로 접근할 수 있음
for data in zip(h_days, e_days):
    print("요일({} -> {})".format(*data))
print("=" * 50)

# zip() 함수를 리스트나 사전으로 감싸서 반복문으로 접근할 수 있음
for data in list(zip(h_days, e_days)):
    print("요일({} -> {})".format(*data))

################ for 문 – enumerate() ################
 # enumerate() 함수를 이용한 for 문
# enumerate() 내장 함수는 컨테이너 객체가 가진 요소의 index와 값을
# 하나의 튜플로 저장한 리스트[(0, "강감찬"), ... ] 객체로 반환한다.
l = ["강감찬", "김유신", "이순신"]

list(enumerate(l))

for i, name in enumerate(l):
    print(i, " - ", name)
print()

# 튜플도 컨테이너 객체이므로 위와 같이 index와 값을
# 하나의 튜플로 저장한 리스트[(0, "사과"), ...]를 반환한다.
t = ("사과", "바나나", "한라봉")

list(enumerate(t))

for i, fruit in enumerate(t):
    print(i, " - ", fruit)
print()

############### for 문 – 중첩 for 문 ###############

# 사전도 컨테이너 객체이며 사전은 index와 키가 하나의
# 튜플로 저장한 리스트[(0, "홍길동"), ...]를 반환한다.
d = {"홍길동": "A", "임꺽정": "C", "장길산": "B"}

list(enumerate(d))

for index, key in enumerate(d):
    print(index, " - ", key, " - ", d.get(key))

# for 문을 여러 개 중첩하여 사용 - 중첩 for 문
for i in range(2, 4):
    for j in range(2, 10):
        print(i, ' x ', j, ' = ', i * j)
    print()

########### for 문 – break와 continue ###########

# break는 현재 수행중인 반복문을 빠져 나감
for i in range(10):
    if i > 5:
        break
    print(i, end=", ")
print()

# continue는 현재 수행중인 반복문의 시작 부분으로 이동함
for i in range(10):
    if i < 7:
        continue
    print(i, end=", ")

print()
########### while 문 ###########

# 조건이 참인 동안 while 블록을 반복 수행
cnt = 1

while cnt <= 10:
    print(cnt, end=", ")
    cnt = cnt + 1
print()

# else 문은 for문과 마찬가지로 while 문이 정상 수행되면 실행된다.
# 중간에 break에 의해 종료되면 수행되지 않는다
sum = 0
cnt = 1

while cnt <= 10:
    sum += cnt
    cnt += 1
else:
    print("1~10 합 :", sum)