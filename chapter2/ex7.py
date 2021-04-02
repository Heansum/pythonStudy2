import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

movie_in = soup.find_all("td", class_="range ac")
for movie in movie_in:
    name = movie.text

    print(name)













