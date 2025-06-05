import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# gera o grafico em uma janela separada
plt.show()

sns.set(style='whitegrid')

pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

# Criando um DataFrame simples a partir de um dicionário
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Idade': [28, 34, 29, 42],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

df_exemplo = pd.DataFrame(dados)

print(df_exemplo.info())

# Simulando a leitura de um CSV com dados faltantes e tipos variados
dados_simulados = {
    'ID': [1, 2, 3, 4, 5],
    'Nome': ['Alice', 'Bob', 'Carlos', None, 'Eva'],
    'Idade': [25, 30, np.nan, 22, 29],
    'Salario': ['5000', '6000', '5500', '5200', '5800']  # armazenados como string
}
df_simulado = pd.DataFrame(dados_simulados)
print("Data frame simulado:")
print(df_simulado)

# Tratamento de dados:
# 1. Remover linhas com valores ausentes em 'Nome' ou 'Idade'
df_limpo = df_simulado.dropna(subset=['Nome', 'Idade'])
print("\nData frame após remover linhas com valores ausentes:")
print(df_limpo)

# 2. Converter a coluna 'Salario' de objeto para numérico
print("Conversão concluida!")
df_limpo['Salario'] = pd.to_numeric(df_limpo['Salario'])
print(df_limpo)

# Criando um DataFrame de exemplo para vendas
dados_vendas = {
    'Loja': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B'],
    'Vendas': [250, 300, 150, 400, 500, 450, 320, 280],
    'Mês': ['Jan', 'Fev', 'Jan', 'Fev', 'Jan', 'Fev', 'Mar', 'Mar']
}
df_vendas = pd.DataFrame(dados_vendas)
print("\nData frame de vendas:")
print(df_vendas)

# Agrupando por Loja para calcular a média de vendas

df_media_vendas = df_vendas.groupby('Loja')['Vendas'].mean().reset_index()
print("\nMédia de vendas por loja:")
print(df_media_vendas)

# Criando uma Pivot Table: Vendas por Loja e Mês

df_pivot_table = df_vendas.pivot_table(values='Vendas', index='Loja', columns='Mês',aggfunc='sum', fill_value=0)
print("\nPivot Table de vendas (Loja x Mês):")
print(df_pivot_table)