import requests
from bs4 import BeautifulSoup

param_dic = {}

fullUrl = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20210401"
fullURL = fullUrl.split("?")

URL = fullURL[0]

parameter = fullURL[1]
parameter = parameter.split("&")

for param in parameter:
    param = param.split("=")

    param_dic[param[0]] = param[1]

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")

movie = []

movieTagList = soup.find_all("td", class_="title")
for movieTag in movieTagList:
    name = movieTag.text
    movie.append(name.strip())

print(movie)

for i in range(0, len(movie)):
    print("{}위: {}".format(i+1, movie[i]))

rangeList = []

rangeTagList = soup.find_all("td", class_="range ac")
for rangeTag in rangeTagList:
    print(rangeTag.text)
    rangeList.append(rangeTag.text)

'''
변동폭의 상승 하락 여부에 상관없이
순위에 변동이 생긴 앱 이름만 출력하세요
'''

if rangeList[i] != int(0):
    print("{}위 : {} / {}".format(i+1, movie[i], rangeList[i]))


for i in range(0, len(movie)):
    if int(rangeList[i]) != 0:
        print("{}위 : {} / {}".format(i+1, movie[i], rangeList[i]))















