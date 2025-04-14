# dictionary 생성
# 변경할 수 없는 데이터(문자열, 숫자, 튜플)를 키로 사용할 수 있음
d = {"name": "홍길동", "age": 25, "gender": "남성"}

# 사전에 새로운 항목을 추가하거나값을 변경할 때 키를 사용함
d["grade"] = 4
d["age"] = 100
print(len(d), " - ", d)

# 사전에서 데이터를 읽어 올 때도 키를 사용함
print(d["name"], d["grade"])

# 사전에서 지정한 키 값이 있는지 확인 –맴버쉽 테스트
print("name" in d)
# 두 개의 요소를 가진 리스트로 구성된 리스트를 사전으로 변환
m = [["name", "이순신"], ["gender", "남성"]]
member = dict(m)
print(member)

# zip() 함수는 두 개의 시퀀스형 자료를 index 순서대로
# 한 쌍으로 묶어서 튜플로 만들어 주는 함수
keys= ["one", "two", "three"]
values = (1, 2, 3)
print(list(zip(keys, values)))
print(dict(zip(keys, values)))

# 사전에서 키만 추출해 리스트로 얻을 수 있음 -순서 없음
print(d.keys())

# 사전에서 값만 추출해 리스트로 얻을 수 있음
print(d.values())

# 사전에서 키와 값 쌍의 데이터를 튜플의 리스트로 얻을 수 있음
print(d.items())

for t in d.items():
    print(t[0], t[1])
# 사전 d를 복사해 새로운 사전을 d2에 할당
d2 = d.copy()
print(d2)

# id() 함수는 파이썬 인터프리터가 관리하는 변수의 참조 값을 반환
print(id(d), " - ", id(d2))

# get() 메서드는 지정한 키에 해당하는 값을 읽어 온다.
print(d2.get("gender"), " - ", d2["gender"], " - ", d2)

# 새로운 사전을 생성한다.
phone = {"홍길동" : "010-5678-5231", "이순신": "010-8956-2347"}
phone2 = {"강감찬": "011-9856-7541"}
phone3 = {"홍길동": "011-1234-5678"}

# 사전 결합하기 - phone의 항목으로 phone2를 추가한다.
phone.update(phone2)
print(phone)

# 사전의 키는 중복될 수 없으므로 같은 값의 키를 가진
# 데이터가 추가되면 이전의 데이터를 덮어 쓴다.
phone.update(phone3)
print(phone)

# del() 함수를 이용해 사전에서 특정 항목을 삭제
del(phone["홍길동"])
print(phone)

# 사전의 모든 항목을 비운다.
phone.clear()
print(phone)