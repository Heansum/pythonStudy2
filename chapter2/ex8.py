import requests

url = "https://play.google.com/store?hl=ko"

response = requests.get(url)
html = response.text

file = open("C:/Users/ITPS/Desktop/index.html", "w", encoding="UTF-8")
file.write(html)
file.close()






