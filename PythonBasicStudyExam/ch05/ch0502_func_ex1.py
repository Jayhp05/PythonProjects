# 람다 함수를 이용해 1 ~ 10까지 제곱하여 모두 더한 값을 출력하시오
# reduce() 함수를 이용하면 편리함
#
# 프로그램 실행 결과
# 385

from functools import reduce

result = reduce(lambda x, y: x + y**2, range(1, 11))

print(result)