import requests
from bs4 import BeautifulSoup

for i in range(1, 1611):
    link = f"https://www.dicio.com.br/palavras-mais-buscadas/{i}/"
    html = requests.get(link).content

    soup = BeautifulSoup(html, 'html.parser')

    words = soup.find("ul", class_="list")

    print(i)

    with open("dicio.txt", "a") as file:
        for li in words.find_all("li"):
            a = li.find("a")
            file.write(a.text + '\n')
