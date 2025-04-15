# time 모듈의 sleep() 함수를 임포트
from time import sleep

# 생성자는 객체가 생성 될 때 초기 값 등을 설정하기 위해 사용된다.
# 소멸자는 객체가 소멸될 때 필요한 작업을 수행하기 위해 사용된다.
# 파이썬은 메서드 오버로딩을 지원하지 않기 때문에 같은 이름의 생성자,
# 소멸자 또는 메서드를 정의할 수 없다.
class Human:
    # 생성자 정의 -생성자, 소멸자의 첫 번째 인수에 self가 있어야 함
    # self는 메모리에 생성되는 인스턴스 자신의 레퍼런스를 가진다.
    def __init__(self, name):
        self.name=name

    # 소멸자 정의
    def __del__(self):
        print("Human 인스턴스 소멸됨")

# 전역 함수 정의
def test():
    h = Human("홍길동")
    sleep(3)

test()