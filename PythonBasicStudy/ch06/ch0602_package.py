import sys
# 파이썬 시스템의 PATH 정보를 출력

# for path in sys.path:
#     print(path)

from  PythonBasicStudy.calculator.Hello import hello, message

hello("홍길동")
message()

import PythonBasicStudy.calculator.adder.cal.MyMul as My

print(My.multiple(10, 20))
# MyAdd 모듈내에 있는 모든 이름을 가져온다.
from PythonBasicStudy.calculator.adder.MyAdd import *

print(add(10, 20), " - ", addMultiNum(1, 2, 3, 4, 5))
from PythonBasicStudy.calculator.ext.cal import ExtAdd as a, ExtMul as m

print(a.add_list(range(1, 11)))
print(m.mul_list(range(1, 6)))