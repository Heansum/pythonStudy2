import requests

# https://movie.naver.com/movie/bi/mi/basic.nhn?code=161967#

# 앞서 사용했던 방법대로 URL을 분석해서
# 자원의 경로와 파라미터를 프로그램이 분리해서 저장하도록 하세요




#fullURL = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=161967#"

param_dic = {}
fullURL = "https://movie.naver.com/movie/sdb/rank/rpeople.nhn"
fullURL = fullURL.split("?")
try:
    URL = fullURL[0]

    parameter = fullURL[1]
    parameter = parameter.split("&")

    for param in parameter:
        param = param.split("=")

        param_dic[param[0]] = param[1]

except IndexError:
    print("파라메터가 없는 URL입니다.")

response = requests.get(URL, param_dic)
print(response.text)
'''
file = open("C:/Users/ITPS/Desktop/response.txt", "w")
file.write(response.text)
file.close()
'''






