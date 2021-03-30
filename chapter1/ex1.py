'''
예외 처리의 필요성
- 프로그램 실행 중 예외가 발생하면
  프로그램이 그 즉시 종료
- 예외로 인해서 컴퓨터가 망가질 수 있음

- 예외가 발생했을 때 컴퓨터의 손상을 방지하고
  우리가 의도한대로 동작하도록 하는 것 -> 예외처리

try:
 예외가 발생할 가능성이 있는 코드
except:
 예외가 발생했을때 처리할 코드
'''

# 예외에 따라서 사용자에게 어떻게 잘못됬는지 알려주는
# 친절한 예외처리를 구현
# 예외의 이름을 알아야 예외에 따라서 적절한 처리를 할 수 있음
# 1. 분모에 0을 입력했을 때
# 2. 분모 또는 분자에 정수가 아닌 실수를 입력했을 때





try:
    print("분자 : ", end="")
    # int() -> 문자열로된 정수 또는 실수값 또는 그외의 숫자 범위에 있는 데이터들
    a = int(input())
    
    print("분모 : ", end="")
    b = int(input())

    result = 0

    result = a / b

    print("{} / {} = {}".format(a, b, result))
    print("try 끝")
except ValueError:
    print("분자와 분모는 정수만 입력 가능합니다.")
except ZeroDivisionError:
    print("분모는 0이 와서는 안됩니다. 다른 정수 값을 입력해주세요.")

print("프로그램 끝")

'''
if b == 0:
    print("다시 입력해주세요 0은 안됩니다.")
else:
    result = a / b
    print("{} / {} = {}".format(a, b, result))

print("프로그램 끝")
'''

