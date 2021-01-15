import requests
from bs4 import BeautifulSoup

for i in range(1, 51):
    link = "https://www.conjugacao.com.br/verbos-populares/" + str(i) + "/"
    html = requests.get(link).content

    soup = BeautifulSoup(html, 'html.parser')

    verbs = soup.find_all("a", title=True)

    print(i, verbs[0].text)

    for j in verbs:
        with open("verbos.txt", "a") as file:
            file.write(j.text + '\n')
            file.close()
