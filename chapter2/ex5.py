import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rpeople.nhn"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

movie_in = soup.find_all("td", class_="title")
for movie in movie_in:
    name = movie.text

    print(name)
    

print(movie_in)







