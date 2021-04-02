import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/basic.nhn"
param_dic = {"code": 10016, "query": "나 홀로 집에"}

response = requests.get(url, param_dic)

try:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")


    review_list = soup.find("div", class_= "score_reple")
    print("===== [ find ] =====")
    print(review_list)

    review_list = soup.find_all("div", class_ = "score_reple")
    print("===== [ find_all ] =====")
    print(review_list)

    for review in review_list:
        reviewContent = review.find("p")
        reviewContent = review.text()
        reviewContent = review.get_text()
        reviewContent = reviewContent.strip()
        print(review.get_text())

except:
    print("데이터를 불러오지 못했습니다.")







