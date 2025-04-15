# matplotlib 패키지는 Python 시각화 기본 패키지
# 시각화 패키지 중 하나인 seaborn 패키지 임포트 
import matplotlib.pyplot as plt
import seaborn as sns

# iris 데이터 세트 로드
iris = sns.load_dataset("iris")
print(iris.head())

# 객체의 데이터 타입 확인
type(iris)

# 데이터 요약 정보 확인
iris.info()

# 수치 데이터 기초통계 확인
iris.describe()

# 범주형 데이터 기초통계 확인
iris.describe(include="object")

# 파이썬 데이터 분석에서 많이 사용하는 자료구조는 2차원의
# DataFrame이며 파이썬에서 가장 유명한 머신러닝 패키지인 
# scikit-learn에서도 DataFrame을 많이 사용하며 지도학습 모델에서는 
# data(2차원의 특징 행렬)와 label(1차원 대상 배열)로 나눠서 사용한다.
x_iris = iris.drop("species", axis=1)
y_iris = iris["species"]
print(x_iris.shape, " - ", y_iris.shape)

# 각 변수의 조합에 대해 그리드(grid) 형태로 히스토그램과 산점도를 그린다.
sns.pairplot(iris, hue="species", height=2)

# seaborn의 차트를 matplotlib의 pyplot를 이용해 화면에 표시한다.
plt.show()