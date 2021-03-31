class HourError(Exception):
    pass

class WrongEmailError(Exception):
    pass

class DuplicateEmail(Exception):
    pass

print("이메일을 입력하세요: ", end="")
email = input()

try:
    # 시간을 잘못입력 했을 때
    raise HourError('시간이 잘못되었습니다.')
    # 이메일을 잘못입력했을 때
    raise ValueError('이메일을 잘못 입력하셨습니다.')
    # 이메일 중복
    raise NameError('이메일이 중복되었습니다.')

    # 비밀번호가 8자리 미만일 때
    # 이름이 10자를 초과했을 때
    # 생년월일이 정상적이지 않을  때
    raise Exception('입력값이 잘못되었습니다.')
except Exception as Msg:
    print(Msg)

print(email)






