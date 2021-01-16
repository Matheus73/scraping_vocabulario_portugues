import requests
from bs4 import BeautifulSoup


for i in range(1, 51):
    link = f"https://www.conjugacao.com.br/verbos-populares/{i}/"
    html = requests.get(link).content

    soup = BeautifulSoup(html, 'html.parser')

    verbs = soup.find_all("a", title=True)

    print(i, ', '.join(v.text for v in verbs))

    with open("verbos.txt", "a") as file:
        for j in verbs:
            file.write(j.text + '\n')
