# Web Scraping Vocabulário Português-Br

## O que é?

Vocabulário contendo palavras em português (pt-br) feito para suprir a falta de materiais de qualidade com esse tipo de conteúdo.

Em uma busca pela internet encontrei vocabulários menores e com alguns problemas, o mais completo que encontrei foi o seguinte:
    
* [ime usp](https://www.ime.usp.br/~pf/dicios/index.html)

Possuindo no total **261798 palavras**.


Para a construção do vocabulário foram usados como base os seguintes sites:

* [Dicio](https://www.dicio.com.br/)
* [Conjugacao](https://www.conjugacao.com.br/)


## Arquivos
| Arquivo | Conteúdo | Número de palavras |
| --- | --- | --- |
|verbos.txt| Verbos no infinitivo | 5000 |
| conjugacao.txt | Todas as conjugações dos verbos do arquivo `verbos.txt`| 461534 |
| dicio.txt | Palavras encontradas no site [Dicio](https://www.dicio.com.br/) | 159704 |
| vocabulario.txt| Arquivo final | 691259  |


### verbos.txt

Arquivo contém 5000 verbos oriundos do site [conjugacao](https://www.conjugacao.com.br/).

O script usado para a sua geração se encontra em: `Scripts/verbos.py`

### conjugacoes.txt

Arquivo contém todos os verbos existentes no arquivo `verbos.txt` junto com suas devidas
conjugações.

O script usado para a sua geração se encontra em: `Scripts/conjugacoes.py`

### dicio.txt

Arquivo contendo todas as palavras contidas no site [Dicio](https://www.dicio.com.br/).

__(PS: Foram retiradas expressões com mais de uma palavra e nomes)__

O script usado para a sua geração se encontra em: `Scripts/dicio.py`

### vocabulario.txt

Arquivo contendo a junção de três arquivos, sendo estes:

* conjugacoes.txt
* dicio.txt
* Vocabulário encontrado no [ime usp](https://www.ime.usp.br/~pf/dicios/index.html)

Com o resultado desses Web scraping foi possivel adicionar **429461 palavras ao vocabulario base.**

