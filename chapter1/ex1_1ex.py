scores = [55, 38, 94, 71, 60]

# 일반적인 값을 입력했을 때
# 일반적이지 않은(예외)값을 입력했을 때

try:
    print("성적을 출력할 학생의 번호 : ", end="")
    number = int(input())

    length = len(scores)

    score = scores[number - 1]
except NameError as errorMsg:
    print(errorMsg)
except ValueError as msg:
    print(msg)
    print("정수 값을 입력해주세요.")
except IndexError as message:
    print(message)
    print("학생 번호는 1 ~ ", length, "까지 있습니다.")
else:
    print(number, "번 학생의 성적은 ", score, "점 입니다.")
finally:
    print("프로그램을 종료합니다.")

'''
ValueError:
IndexError:
if number < 0 or number >= length:
    print("잘못 입력 하셨습니다")
    print("학생 번호는 1 ~ ", length, "까지 있습니다.")
else:
    score = scores[number-1]
    print(number, "번 학생의 성적은 ", score, "점 입니다.")
'''
