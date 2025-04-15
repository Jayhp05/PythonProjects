################ 메서드 정의 ################

# 클래스 안에 정의한 함수를 메서드라 부름
# 메서드의 첫 번째 인수에 self가 지정되면 인스턴스 메서드 임
# self는 메모리에 생성되는 인스턴스 자신의 레퍼런스를 가진다.
class Human:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

h = Human()
h.setName("이순신")
h.setAge(35)
print(h.getName(), " - ", h.getAge())

# 클래스를 이용한 인스턴스 메서드 실행
h1 = Human()

# 메서드의 self 인수 자리에 인스턴스의 레퍼런스를 지정해야 함
Human.setName(h1, "강감찬")
Human.setAge(h1, 45)

# 새로운 인스턴스 멤버를 인스턴스 이름공간에 등록
h1.gender = "남성"
print(h1.getName(), " - ", h1.getAge(), " (", h1.gender, ")")

# 전역 함수 정의
def setNum(num):
    print("전역 함수 : ", num + 1)

# 인스턴스 메서드와 변수 접근 시에 반드시 self를 사용해 접근해야 함
class MyClass:
    def setNum(self, num):
        self.num = num

    def getNum(self):
        return self.num

    def increment(self):
        self.setNum(self.num + 1)

    def outIncr(self):
        # 전역영역의 이름공간에서 함수를 찾는다.
        setNum(self.num + 10)

c = MyClass()
c.setNum(10)
c.increment()


print("인스턴스 변수 num :", c.getNum())
c.outIncr()

################### 정적 메서드 ###################

# 정적 메서드는 인스턴스와 무관하게 클래스 이름공간에 존재하는 메서드
# @staticmethod 라는 장식자(Decorator)를 메서드 위에 지정한다.
# 클래 메서드는 정적 메서드와 같이 클래스 이름공간에 존재하는 메서드
# @classmethod 라는 장식자(Decorator)를 메서드 위에 지정한다.
# 정적 메서드와 클래스 메서드는 첫 번째 인수로 self를 사용할 수 없다.
class M:
    @staticmethod
    def staticMessage(x):
        print("정적 메서드 :", x)

    # 클래스 메서드와 정적 메서드의 다른 점은
    # 첫 번째 인수로 클래스 객체를 자동으로 받는다.
    @classmethod
    def classMessage(cls, x):
        print("클래스 메서드 :", cls, " - ", x)

# 정적 메서드와 클래스 메서드는 인스턴스 변수를 이용해 접근이 가능함
sm = M()
sm.staticMessage("안녕 파이썬")
sm.classMessage("Hi Python")

# 정적 메서드와 클래스 메서드는 클래스 이름으로 바로 접근할 수 있다.
M.staticMessage("쉬운 파이썬")
M.classMessage("Easy Python")

# M 클래스를 상속 받는 SM 클래스 정의
class SM(M):
    pass

# 상속 받는 서브 클래스에서 클래스 메서드를 호출하면
# 서브 클래스 객체가 첫 번째 인수로 자동 할당된다.
SM.staticMessage("상속 받은 SM")
SM.classMessage("상속 받은 SM")