from bs4 import BeautifulSoup
import requests

verbs = []

with open("verbos.txt") as f:
    for line in f:
        line = line.strip()
        verbs.append(line)

for l, i in enumerate(verbs):

    html = requests.get("https://www.conjugacao.com.br/verbo-" + i).content

    soup = BeautifulSoup(html, 'html.parser')

    conj = soup.find_all("span", class_="f")

    print(l)

    for j in conj:
        with open("conjugacoes.txt", "a") as file:
            file.write(j.text + '\n')
            file.close()
