# 모듈 : 소스파일

# 모듈 안에 있는 모든 소스코드를 불러옴
# import Calc

# Calc 모듈 안에 있는 minus 함수만 불러옴
# from Calc import minus
# from ~ import 를 사용해서 특정 함수 또는 코드만 불러왔을 때는
# 모듈명을 명시하지 못한다.
# Calc.minus -> 이렇게 안됨
# minus(1, 2)

# 프로그래밍에서 * -> 모든을 의미
# 프로그래밍에서 (1~9) -> 선택지
# 프로그래밍에서 [1~9] -> 범위
# from Calc import *

# Calc.minus -> minus plus 로 대체

# 모듈에 별명을 붙이기
# 모듈의 이름이 중복되었을 때 모듈을 서로 구분하기 위한
# 별명을 붙일 수 있음
# import 모듈명 as 별명
import Calc as MyCalc
# 모듈 내 특정 함수 또는 소스코드에도 별명을 붙일 수 있음
from Calc import minus as MyMinus
MyMinus(1, 2)










