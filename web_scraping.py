import requests
from bs4 import BeautifulSoup
import csv

# Começamos pela primeira página
url_base = "http://books.toscrape.com/catalogue/"
url_atual = "http://books.toscrape.com/catalogue/page-1.html"
dados_all_livros = []

while url_atual:
    print(f"Coletando dados de: {url_atual}")
    resposta = requests.get(url_atual)
    sopa = BeautifulSoup(resposta.text, 'html.parser')

    # Coleta os livros da página atual
    livros = sopa.find_all('article', class_='product_pod')
    for livro in livros:
        titulo = livro.h3.a['title']
        preco_texto = livro.find('p', class_='price_color').text
        preco_num = float(preco_texto.replace("£", "").replace("Â", "").strip())
        
        dados_all_livros.append({"Título": titulo, "Preço (GBP)": preco_num})

    # PROCURA O BOTÃO 'NEXT'
    botao_proximo = sopa.find('li', class_='next')
    
    if botao_proximo:
        # Se achou, monta a URL da próxima página
        proxima_pagina = botao_proximo.a['href']
        url_atual = url_base + proxima_pagina
    else:
        # Se não achou o botão, a url_atual vira None e o loop para
        url_atual = None

# SALVANDO TODOS OS DADOS (Agora de todas as páginas!)
with open('todos_os_livros.csv', 'w', newline='', encoding='utf-8') as arquivo:
    colunas = ['Título', 'Preço (GBP)']
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(dados_all_livros)

print(f"Sucesso! {len(dados_all_livros)} livros coletados e salvos.")