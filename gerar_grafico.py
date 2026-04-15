import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados do CSV que você criou
df = pd.read_csv('todos_os_livros.csv')

# 2. Criar um histograma para ver a distribuição dos preços
plt.figure(figsize=(10, 6))
plt.hist(df['Preço (GBP)'], bins=20, color='skyblue', edgecolor='black')

# 3. Personalizar o gráfico
plt.title('Distribuição de Preços dos Livros Coletados', fontsize=15)
plt.xlabel('Preço (£)', fontsize=12)
plt.ylabel('Quantidade de Livros', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# ... código anterior ...

# 4. Salvar o gráfico como imagem para o seu portfólio
plt.savefig('grafico_precos.png')
print("Gráfico 'grafico_precos.png' gerado com sucesso!")
plt.close() # <-- ADICIONE ESTA LINHA AQUI

# 5. Mostrar o gráfico na tela (pode continuar falhando, mas o arquivo já estará salvo)
# plt.show() # Você pode até comentar esta linha com um '#' se não for usar

# 5. Mostrar o gráfico na tela
plt.show()