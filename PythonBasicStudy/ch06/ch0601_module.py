# import 문을 사용해 모듈을 불러온다.
# 프로젝트의 루트를 기준으로 모듈의 위치를 지정할수 있고
# 같은 패키지에 있는 모듈은 모듈 이름만 지정해 사용할 수 있다.
import MyCalc

# MyCalc 모듈에 존재하는 모든 이름의 리스트를 출력
print(dir(MyCalc))
print(MyCalc.MyPi)
print(MyCalc.area(10))

# 모듈을 불러오고 모듈에 정의된 이름을 현재 이름공간에 불러온다.
# from MyCalc import * 와 같이 각각의 이름을 지정하지 않고
# * 를 사용하면 __로 시작하는 이름을 제외한 모든 이름을 불러온다.
from MyCalc import area, MyPi, multiple

print(multiple(10, 20))
print(area(100))

# 모듈, 클래스, 함수 등에 별칭을 붙여 간단하게 사용할 수 있으며
# 모듈 이름이 충돌할 경우 유용하게 사용할 수 있는 방법이다.
# from MyCalc import area as a, MyPi as p
import MyCalc as my
print(my.MyPi, " - ", my.multiple(10, 20))

# 현재 모듈이 최상위 모듈(import가 아닌)로 실행되는지 아니면
# 다른 모듈에 의해 import 되어 실행되는지 구별하기 위해 사용함
# 최상위 모듈로 실행되면 __main__ 값이 __name__에 할당된다.
print(__name__)

# import 되어 실행될 때 __name__에 모듈의 이름이 할당된다.
print(my.__name__)

# 모듈을 개발할 때 모듈을 테스트 하는 코드로 사용
if __name__ == "__main__":
    print("현재 모듈이 최상위에서 실행됨")