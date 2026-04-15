import requests
from bs4 import BeautifulSoup
import csv # Biblioteca para salvar o arquivo

# 1. ACESSAR O SITE
url = "http://books.toscrape.com/"
resposta = requests.get(url)
sopa = BeautifulSoup(resposta.text, 'html.parser')

# 2. ENCONTRAR OS PRODUTOS
livros = sopa.find_all('article', class_='product_pod')
dados_livros = []

for livro in livros:
    titulo = livro.h3.a['title']
    preco_texto = livro.find('p', class_='price_color').text
    # Limpamos o preço: tiramos o £ e convertemos para número
    # Isso remove o símbolo da libra e qualquer caractere estranho que venha junto
    preco_num = float(preco_texto.replace("£", "").replace("Â", "").strip())
    
    # Guardamos em um dicionário
    dados_livros.append({
        "Título": titulo,
        "Preço (GBP)": preco_num
    })

# 3. SALVAR EM CSV (O que você tentou digitar no terminal)
# Criamos um arquivo chamado 'precos_livros.csv'
with open('precos_livros.csv', 'w', newline='', encoding='utf-8') as arquivo:
    colunas = ['Título', 'Preço (GBP)']
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    
    escritor.writeheader() # Escreve o cabeçalho
    escritor.writerows(dados_livros) # Escreve os dados

print("Arquivo gerado com sucesso!")