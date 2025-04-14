# 사용자로부터 직사각형의 폭과 높이를 입력 받아 직사각형의 둘레 및 넓
# 이를 구하여 사전(dict) 데이터로 반환하는 함수 rect_area()를 정의하고
# 테스트 하시오.
#
# 아래와 같이 호출하면 사전 데이터를 반환 받는다.
# d = rect_area()

# 1. rect_area() 함수를 실행한 결과
# 사각형의 폭을 입력해 주세요(m)
# >? 10
# 사각형의 높이를 입력해 주세요(m)
# >? 20

# 2. 반환 받은 d(사전 데이터)를 출력한 결과 –문자열 포맷터를 이용할 것
# 폭 : 10, 높이 : 20인 사각형의 둘레 : 60m, 면적 : 200㎡

def reat_area():
    w = int(input("사각형의 폭을 입력해 주세요(m)\n>? "))
    h = int(input("사각형의 높이를 입력해 주세요(m)\n>? "))

    p = 2 * (w + h)
    a = w * h

    return {"width": w, "height": h, "perimeter": p, "area": a}

d = reat_area()

print(f"폭 : {d["width"]}, 높이 : {d["height"]}인 사각형의 둘레 : {d["perimeter"]}m, 면적 : {d["area"]}㎡")
