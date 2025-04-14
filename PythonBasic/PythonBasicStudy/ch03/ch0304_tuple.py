########## 튜플(tuple) ##########
# tuple 생성
months = ('Jan', 'Feb','Mar', 'Apr', 'May', 'Jun',
'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# 리스트와 마찬가지로 인덱싱과 슬라이싱이 가능함
print(months[0], months[:-1], months[0:], months[:], months[::2])
print(len(months), type(months))

# 튜플을 리스트로 형 변환
print(list((1, 2, 3)))

# 튜플은 리스트와 달리 수정 할 수 없기 때문에 에러가 발생한다.
# 튜플은 한 번 생성되면 요소의 추가, 수정, 삭제를 할 수 없다.
# months[0] = 100
# months[0:2] = ()
# 튜플을 2만큼 반복하여 하나의 리스트로 반환
print(months * 2)
# 튜플에 튜플을 연결해 새로운 하나의 튜플로 반환
print(months + (2, 3))

# 튜플 months 안에 Dec가 존재하는지 여부
print("Dec" in months)

# 튜플과 리스트를 생성
t1 = (1, 2, 3, 4, 5)
l1 = [1, 3, 5]

# 튜플 안의 요소로 튜플, 리스트 등을 가질 수 있음
# 튜플 안에 여러 개의 데이터를 저장하는 것을 패킹(packing)이라 함
t = (7, 8, t1, l1)
print(t, " : ", t[2][3], " : ",  t[2][::-1])

# 튜플을 이용해 여러 변수에 값을 할당할 수 있음
# 이것을 언패킹(tuple unpacking)이라 함
gu = ("강서구", "양천구", "구로구")
a, b, c = gu
print(a, b, c)