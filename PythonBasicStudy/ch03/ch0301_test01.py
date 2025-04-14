# 포맷팅 출력 방법 : %, .format, f
name = "홍길동"
age = 25
print("name=%s, age=%s"%(name, age))
print("%10d, %10f, %10s"%(123, 123, 123))
print("%3.5d, %5.2f, %1.5f"%(123, 123, 123))

print("이름 : {}, 나이 : {}".format(name, age))
print("이름 : {0}, 나이 : {1}".format(name, age)) # 순서 지정해서 삽입 가능

print(f"이름 : {name}, 나이 : {age}")

# 리스트
l = {1, 2, 3, 4, 5}
print(l[1], l[2:4], l[2:])
print(2 in l)

l.append(10)
print(l)

# 튜플
## 리스트 거의 같은 저장 순서를 유지 - 튜플 수정X
t1 = (1, 2, 3)
l1 = list(t1)
a, b, c = t1
print(t1, " - ", l1)

# 사전 dict
d = {"name": "홍길동", "age": 25}
print(d["name"], " = ", d.get("name"))
d["gender"] = "남성"
print(d)
print(d.keys(), d.values())