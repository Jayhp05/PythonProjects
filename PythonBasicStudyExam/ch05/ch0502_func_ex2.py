# 다음과 같은 리스트가 있을 때 람다 함수를 이용해 이 리스트의 홀수만
# 필터링 하여 홀수의 총합을 구하는 프로그램을 작성하시오

# filter() 함수와 reduce() 함수를 이용하면 편리함
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

# 프로그램 실행결과
# [1, 3, 5, 7, 9]
# 25

from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = list(filter(lambda x: x % 2 != 0, l))

odd_sum = reduce(lambda x, y: x + y, odd_numbers)

print("프로그램 실행결과")
print(odd_numbers)
print(odd_sum)
