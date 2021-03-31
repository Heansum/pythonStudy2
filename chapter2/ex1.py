import requests

# URL -> Uniform Resource Locater
# 자원이 위치한 경로
# 프로토콜 ://도메인:포트번호/경로
# 프로토콜 : 자원이 위치한 경로로 접근할 때 어떤 방법으로 접근할 것인가
# 도메인   : 자원이 위치한 인터넷 주소
#           0~255 3자리의 한 묶음을 4개로 묶어서 표현한 것
# 포트번호 : 해당 자원으로 접속하기 위한 포트번호
#           (0 ~ 66,535번)
# 경로 : 해당 자원이 위치한 추가적인 경로
url = 'https://www.naver.com/'

response = requests.get(url)

print("응답코드 : {}".format(response.status_code))
print(response.text)

# 버스를 타고 부산진구 중앙대로 668, 4층으로 간다.
# 4층에 와서 인포데스크의 자동문으로 들어간다.







