# Importando bibliotecas essenciais
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o ambiente para exibição de gráficos no notebook
#%matplotlib inline
sns.set(style='whitegrid')
pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

#Exemplo de Merge
df_clientes = pd.DataFrame({
    'ClienteID': [1, 2, 3],
    'Nome': ['Alice', 'Bob', 'Carlos']
})

df_pedidos = pd.DataFrame({
    'PedidoID': [101, 102, 103],
    'ClienteID': [1, 2, 2],
    'Valor': [250, 300, 150]
})

df_merged = pd.merge(df_clientes, df_pedidos, on='ClienteID', how='inner')
#print("Merge de clientes e pedidos:")
#print(df_merged)

#Exemplo de concet (vertical)
df_parte1 = pd.DataFrame({
    'Produto': ['A', 'B'],
    'Preço': [10, 20]
})
df_parte2 = pd.DataFrame({
    'Produto': ['C', 'D'],
    'Preço': [15, 25]
})

df_concat = pd.concat([df_parte1, df_parte2], ignore_index=True)
print("\nConcatenação vertical dos DataFrames:")
print(df_concat)