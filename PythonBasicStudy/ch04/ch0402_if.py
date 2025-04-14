############### if 문 ###############

# 파이썬은 들여쓰기를 강제하여 코드의 가독성을 높이고 있음
# if문의 첫 라인은 메인 블록으로 1열에서 시작해야 하고 콜론(＂:“)을
# 사용해 새 블록의 시작을 알리고 새 블록은 반드시 들여쓰기를 해야 함.

# if 문
score = 60

if score >= 60:
    print("합격")

# if ~ else 문
if score >= 60:
    print("합격")
else:
    print("불합격")

# if ~ elif ~ else 문
score2 = 80

if score2 >= 90:
    print("학점 : A")
elif score2 >= 80:
    print("학점 : B")
elif score2 >= 70:
    print("학점 : C")
else:
    print("학점 : 낙제")

# None, 0, 0.0, “”, [], (), {} 는
# if문의 테스트에서 모두 False를 반환한다. 이외에는 모두 True 반환
if []:
    print("비어 있지 않음")
else:
    print("비어 있음")

if None:
    print("비어 있지 않음")
else:
    print("비어 있음")

