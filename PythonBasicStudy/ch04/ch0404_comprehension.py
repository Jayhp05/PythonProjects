# Comprehension은 하나 이상의 이터레이터(반복 가능한 객체)로부터
# 파이썬의 자료구조(list,tuple,dict 등)를 만드는 함축적 방법을 말한다.
# 컴프리헨션을 사용하지 않고 리스트 만들기
L = []
for i in range(10):
    L.append(i * 2)

print(L)

# 리스트 컴프리헨션을 사용한 리스트 만들기 -리스트 내포
# for 앞에 사용하는 변수는 for 문의 변수와 동일해야 함.
# 0, 1, 2,... 가 i에 할당 될 때 리스트의 항목으로 추가됨
L = [i * 2 for i in range(10)]
print(L)

# 컴프리헨션은 조건식을 가질 수 있음
# 다음은 홀 수만 선택해 리스트의 항목으로 추가하는 예제
L = [i for i in range(11) if i % 2 == 1]
print(L)

# 컴프리헨션은 하나 이상의 for 문을 가질 수 있음
L = []
rows = range(1, 4)
cols = range(1, 4)
for row in rows:
    for col in cols:
        L.append((row, col))
    print(L)

# 컴프리헨션을 사용해 튜플을 리스트의 항목으로 만듦
# 위의 중첩 for 문을 사용해 리스트를 만드는 것 보다
# 컴프리헨션을 사용하는 것이 "더 파이써닉하다."라고 말한다.
cells = [(row, col) for row in rows for col in cols]
print(cells)

# 딕셔너리 컴프리헨션을 이용해 단어 수 세기
L = ["가위", "바위", "보", "가위", "바위", "바위"]
{i:L.count(i) for i in L}

# 셋 컴프리헨션을 사용한 셋 만들기
{ num for num in range(1, 10) if num % 2 == 0 }

# 제너레이터 컴프리헨션 -튜플은 컴프리헨션이 없음
# 제너레이터는 이터레이터에 데이터를 제공하는 객체로
# 제너레이터는 한 번만 실행할 수 있다.
GE = (num for num in range(1, 6))

for i in GE:
    print(i)