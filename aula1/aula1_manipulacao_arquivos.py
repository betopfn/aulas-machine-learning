import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




sns.set(style='whitegrid')

pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

#Exemplo; Escrita e leitura de um csv
df_exemplo_io = pd.DataFrame({
    'Produto': ['A', 'B', 'C'],
    'Preço': [10.5, 20.75, 15.0],
    'Quantidade': [100, 150, 200]
})

#Escrevendo para csv

df_exemplo_io.to_csv("exemplo.csv", index=False)
df_exemplo_io.to_parquet("exemplo.parquet")
print("Arquivo CSV 'exemplo.csv' criado!")

# Lendo o arquivo CSV
df_csv = pd.read_csv("exemplo.csv")
print("\n Conteudo lido do csv")
print(df_csv)

#Exemplo: Escrita e leitura de um arquvi xlsx
# (Requer que a biblioteca openpyxl ou xlsxwriter esteja instalada)
df_exemplo_io.to_excel("exemplo.xlsx", index=False)
print("Arquivo Excel 'exemplo.xlsx' criado!")

# Lendo o arquivo Excel
df_excel = pd.read_excel("exemplo.xlsx")
print("\n Conteudo lido do excel")
print(df_excel)

# Exemplo: Manipulação de JSON
import json
dados_json = {
    "clientes": [
        {"nome": "Ana", "idade": 28},
        {"nome": "Bruno", "idade": 34},
        {"nome": "Carlos", "idade": 29}
    ]
}

# Convertendo o dicionario para string json
json_str = json.dumps(dados_json, indent=2, ensure_ascii=False)


# Convertendo a string JSON de volta para dicionário e criando DataFrame
dados_carregados = json.loads(json_str)
df_json = pd.DataFrame(dados_carregados["clientes"])
print("\n Conteudo criado a partir do json")
print(df_json)