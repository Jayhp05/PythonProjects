##################### 클래스 멤버와 인스턴스 멤버 #####################

# 클래스 멤버는 클래스 이름공간에 생성되고 모든 인스턴스에서 공유가
# 가능하며 인스턴스 멤버는 각각의 인스턴스 이름공간에 생성되고
# 인스턴스 마다 독립적으로 다른 값을 가질 수 있다.
class Score:
    min = 0
    max = 100
    score = 50

    def setScore(self, score):
        if(score < 0 or score > 100):
            print("점수는 0 ~ 100점 까지")
        # self.score = 0
        else:
            self.score = score

    def getScore(self):
        return self.score

# 각각의 인스턴스를 생성하고 인스턴스 메서드를
# 호출해 인스턴스 멤버를 생성한다.
s1 = Score()

# 이 메서드는 0 ~ 100 사이의 점수가 아니므로
# 인스턴스 멤버 score는 생성되지 못한다.
s1.setScore(101)

# s1의 인스턴스 변수 score는 생성되지 않았기 때문에 클래스 멤버인
# score 값이 출력된다. 인스턴스 변수로 score에 접근할 경우
# 인스턴스 이름 공간에서 score를 찾고 인스턴스 이름 공간에 score가
# 없을 경우 클래스 이름 공간에서 score를 찾는다.
print(s1.score)

# 클래스 멤버는 인스턴스 변수와 클래스 이름으로 접근 가능함
print(s1.getScore(), " - ", s1.min, " - ", s1.max)
print(Score.min, " - ", Score.max)