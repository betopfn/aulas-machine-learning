import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




sns.set(style='whitegrid')

pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

# Exemplo 1: Gráficos de Linhas
# Definindo os dados
x = np.linspace(0, 10, 100)
y = np.sin(x)
# Construindo o gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Seno', color='blue', linestyle='-')
plt.title('Gráfico de Linhas: Função Seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()


# Exemplo 2: Gráfico de Barras
# Definindo os dados
categorias = ['A', 'B', 'C', 'D']
valores = [23, 53, 45, 54]
# Construindo o gráfico
plt.figure(figsize=(10, 5))
plt.bar(categorias, valores, color='orange')
plt.title('Gráfico de Barras')
plt.xlabel('categorias')
plt.ylabel('valores')

# Exemplo 3: Histograma
# Definindo os dados
dados_hist = np.random.randn(1000)
# Construindo o gráfico
plt.figure(figsize=(10, 5))
plt.hist(dados_hist, bins=30, color='blue', alpha=0.7)
plt.title('Gráfico de Histograma')
plt.xlabel('Valor')
plt.ylabel('Frequência')

# Exemplo 4: Gráfico de Pizza
# Definindo os dados
labels = ['Frutas', 'Verduras', 'Carnes', 'Laticínios']
sizes = [30, 20, 25, 25]
explode = (0, 0, 0.1, 0)  # explode a terceira fatia
# Construindo o gráfico
plt.figure(figsize=(10, 5))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title('Gráfico de Pizza')
plt.axis('equal')  # A proporção de aspecto igual garante que a pizza seja desenhada como um círculo.
# gera o grafico em uma janela separada
plt.show()





