# 🕸️ Monitor de Preços de Livros com Web Scraping

Este é um projeto de automação desenvolvido em **Python** para coletar dados de preços de uma livraria online. O objetivo é demonstrar habilidades em extração de dados (Web Scraping), tratamento de strings e armazenamento de informações estruturadas.

## 🚀 Tecnologias Utilizadas
* **Python 3.14**
* **BeautifulSoup4**: Para a análise do HTML.
* **Requests**: Para as requisições HTTP.
* **CSV**: Para exportação dos dados coletados.

## 🛠️ Como o projeto funciona
1. O script acessa a URL do e-commerce.
2. Identifica os títulos e preços de cada produto usando seletores CSS.
3. Realiza a limpeza dos dados (remoção de caracteres especiais e conversão para float).
4. Exporta tudo para um arquivo `precos_livros.csv` pronto para análise em Excel.

## 📈 Insights de Aprendizado
Durante o desenvolvimento, lidei com desafios de **encoding** (caracteres especiais no HTML) e aprendi a estruturar laços de repetição para coleta em massa.

## 📊 Resultados do Crawler
* **Total de itens minerados:** 1.000 livros.
* **Tempo de execução médio:** ~15 segundos.
* **Formato de saída:** CSV estruturado.