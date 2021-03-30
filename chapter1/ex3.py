import math

# 올림을 하는 메서드
math.ceil()

# 버림을 하는 메서드
math.trunc()


try:
    height = input("키를 입력하세요 >>> ")
    # round -> 반올림을 하는 함수
    # 사사오입이 적용되는 함수
    # 반올림할 자리의 수가 5 이상 -> 올림
    # 반올림할 자리의 수가 5 이상이면서, 그 앞의 수가 짝수면 내림
    # 반올림할 자리의 수가 5 이상이면서, 그 앞의 수가 홀수면 올림
    # 반올림할 자리의 수가 5 미만 -> 버림
    height = round(height)
    print("입력하신 키는 {}cm로 처리됩니다.".format(height))
except:
    print("예외가 발생하였습니다.")



