##################################################
#################### 상속 ####################
# 상속을 해 주는 클래스 -부모, 슈퍼, 베이스 클래스라 부른다.
class Car:
    def drive(self):
        print("자동차를 운전함")

# 상속받는 클래스 -자식, 서브, 파생 클래스라 부른다.
# 클래스 상속은 아래와 같은 형식으로 클래스를 정의한다.
# class 클래스이름(상속받는 부모 클래스 이름):
class Bus(Car):
    pass

# 부모가 가진 기능을 그대로 사용할 수 있다.
bus1 = Bus()
bus1.drive()

# 부모가 가진 기능을 그대로 사용할 수 있다.
bus1 = Bus()
bus1.drive()

# 객체 타입 비교
print(Bus, " - ", Car, " - ", bus1)
print(type(bus1) == Bus, " - ", type(bus1) == Car)

# 객체의 타입(자료형) 비교
# 상속 관계에 있는 클래스의 인스턴스는 True 반환
# Bus는 Bus 타입이면서 Car 타입이기도 함
print(isinstance(bus1, Bus), " - ", isinstance(bus1, Car))

# 클래스 간의  상속관계 비교 –클래스 이름을 사용
print(issubclass(Bus, Bus), " - ", issubclass(Bus, Car))

# Car 클래스를 상속 받는 Truck 클래스 정의
class Truck(Car):
    # 상속 받은 메서드 또는 생성자를 필요에 의해 자식 클래스에서
    # 다시 정의할 수 있다. 이를 메서드 오버라이드(Override)라 한다.
    # __init__() 생성자를 포함해 모든 메서드를 오버라이드 할 수 있다.
    def drive(self):
        print("Truck을 운전함")

# 메서드 오버라이드를 하면 인스턴스가 가진 메서드가 호출된다.
c = Car()
t = Truck()
c.drive()
t.drive()

class Super():
    def __init__(self, name):
        self.name = name
    print("Super 생성자 호출됨")

# Super 클래스를 상속 받는 클래스
class Sub1(Super):
    pass

# 자식 클래스에 생성자가 정의되어 있지 않으면
# 부모의 생성자가 자식 객체를 생성할 때 자동으로 호출된다.
s = Sub1("강감찬")
print(s.name)

# Super 클래스를 상속 받는 클래스
class Sub2(Super):

    # 생성자가 오버라이드 되면 부모의 생성자는 자동 호출되지 않기
    # 때문에 자식의 생성자에서 명시적으로 호출해야 한다.
    def __init__(self, name):
        Super.__init__(self, name)

# super() 메서드는 부모 클래스(Super)의 정의를 얻는다.
#super().__init__(name)
print("Sub2 생성자 호출됨")
s1 = Sub2("이순신")

print(s1.name)

class Human:

    def __init__(self, name, age, gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    # __str__()는 객체의 현재 상태를 문자열로 표현하는 메서드로
    # 작성자가 인스턴스의 현재 상태를 표현할 수 있도록 작성하면 된다.
    # 인스턴스를 참조하는 변수를 출력하거나 내장 함수인
    # str(참조변수 이름) 함수를 이용하여 출력할 수 있다.
    def __str__(self):
        return "<Human {} {} {}>"\
        .format(self.name, self.age, self.gender)

# Human 클래스를 상속받는 Student 클래스
class Student(Human):
    # 자식 클래스의 생성자 정의
    # 자식 클래스에서 필요한 기능을 추가해 생성자를 다시 정의 했다.
    def __init__(self, name, age, gender, grade):
        # 부모 클래스인 Human의 생성자 호출
        Human.__init__(self, name, age, gender)

        # super() 메서드는 부모 클래스(Human)의 정의를 얻는다.
        #super().__init__(name, age, gender)
        # 자식 클래스에서 속성을 추가함
        self.grade = grade

s1 = Student("홍길동", 35, "남자", 2)
print(s1.name, " - ", s1.grade, " - ", s1, " - ", str(s1))