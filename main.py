from fastapi import FastAPI, Depends, HTTPException, Security, BackgroundTasks
from fastapi.security.api_key import APIKeyHeader
import requests
from bs4 import BeautifulSoup
import httpx # Para o Telegram

app = FastAPI(title="API Monitor com Alerta")

# --- SEGURANÇA ---
API_KEY = "marcelo123"
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# --- CONFIG BOT ---
TELEGRAM_TOKEN = "8708615370:AAGRoGhwVqEWXMZ_TN3CvzR_09srNSda4_Y"
CHAT_ID = "8708615370"

async def enviar_telegram(mensagem: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        await client.post(url, json={"chat_id": CHAT_ID, "text": mensagem})

async def get_api_key(header_key: str = Security(api_key_header)):
    if header_key == API_KEY: return header_key
    raise HTTPException(status_code=403, detail="Acesso Negado")

@app.get("/monitorar")
async def monitorar_com_alerta(bt: BackgroundTasks, token: str = Depends(get_api_key)):
    # 1. Faz o Scraping
    url = "http://books.toscrape.com/catalogue/page-1.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    primeiro_livro = soup.find('article', class_='product_pod').h3.a['title']
    
    # 2. Lógica de Alerta (Exemplo: avisa sempre que rodar)
    alerta_msg = f"✅ Monitoramento Concluído!\n📦 Primeiro livro da lista: {primeiro_livro}"
    
    # 3. Dispara o Telegram em segundo plano (não trava a API)
    bt.add_task(enviar_telegram, alerta_msg)
    
    return {"status": "Processado", "msg": "Alerta enviado ao Telegram!"}
