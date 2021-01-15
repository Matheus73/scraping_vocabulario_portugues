import requests
from bs4 import BeautifulSoup

for i in range(1, 1611):
    link = "https://www.dicio.com.br/palavras-mais-buscadas/" + str(i) + "/"
    html = requests.get(link).content

    soup = BeautifulSoup(html, 'html.parser')

    words = soup.find("ul", class_="list")

    print(i)

    for li in words.find_all("li"):
        a = li.find("a")
        with open("dicio.txt", "a") as file:
            file.write(a.text + '\n')
            file.close()
