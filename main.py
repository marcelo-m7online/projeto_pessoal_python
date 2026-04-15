from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
import requests
from bs4 import BeautifulSoup
from starlette import status

app = FastAPI(title="API Segura de Scraping")

# 1. Definimos o nome da chave que o usuário deve enviar no cabeçalho
API_KEY = "marcelo123" # Esta é a sua senha!
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# 2. Função que valida se a chave está correta
async def get_api_key(header_key: str = Security(api_key_header)):
    if header_key == API_KEY:
        return header_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, 
        detail="Chave de API inválida ou ausente"
    )

@app.get("/")
def home():
    return {"msg": "API Online. Use /docs para testar com sua chave."}

# 3. Aplicamos a trava (Depends) apenas na rota de coleta
@app.get("/coletar-agora")
def coletar_viva(token: str = Depends(get_api_key)):
    url = "http://books.toscrape.com/catalogue/page-1.html"
    resposta = requests.get(url)
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    
    livros_pagina = []
    produtos = sopa.find_all('article', class_='product_pod')
    
    for p in produtos:
        titulo = p.h3.a['title']
        preco = p.find('p', class_='price_color').text
        livros_pagina.append({"titulo": titulo, "preco": preco})
    
    return {"status": "Autorizado", "dados": livros_pagina}