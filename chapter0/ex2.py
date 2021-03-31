# 난수(임의의 수)와 관련된 많은 함수들이 들어있다
import random

# randint -> 임의의 정수 하나를 뽑는 함수
# 1이상 10미만의 임의의 정수 하나를 뽑는 함수
# 첫 번째 매개변수 - 시작 수
# 두 번째 매개변수 - 끝 수
# 시작 수 이상 끝 수 미만 사이의 임의의 정수를 하나 뽑는 함수
print(random.randint(1, 11))

# randrange -> 시퀀스 객체 range()
print(random.randrange(1, 11, 2))

# random
# 0이상 1미만의 실수 중 하나를 뽑는 함수
print(random.random() * 100)

percent = random.random() * 100
print(percent)

# 제비뽑기를 했을 때 30퍼센트의 확률로 당첨이 된다.
if percent < 30:
    print("당첨되었습니다!")
else:
    print("아쉽게도 당첨되지 못했습니다.")

# choice -> 시퀀스객체에서 임의의 한 원소를 뽑고 싶을 때

# sample -> 시퀀스객체에서 지정된 개수의 요소를 임의로 반환
result = random.sample(range(1, 11), 3)
print(result)
