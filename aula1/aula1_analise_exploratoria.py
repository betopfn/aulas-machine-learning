import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




sns.set(style='whitegrid')

pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

#integrando o dataset "Iris" do seaborn
df_iris = sns.load_dataset('iris')

#vizualizando as primeiras linhhas e informações gerais do dataset
print("Primeiras linhas do dataset Iris:")
print(df_iris.head())

#informações do dataset
print("\nInformações do dataset Iris:")
df_iris.info()

# Estatísticas descritivas
print("\nEstatísticas descritivas do dataset Iris:")
print(df_iris.describe())

#vizualizando a distribuição das especie
plt.figure(figsize=(10, 6))
sns.countplot(data=df_iris, x='species', palette='Set2')
plt.title("Contagem de especies")
plt.show()