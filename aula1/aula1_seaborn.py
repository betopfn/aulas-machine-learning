import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

#Usando o dataset tips do seaborn para os exemplos
df_tips = sns.load_dataset('tips')

#Gráfico de dispersão com llinhs de regressão
plt.figure(figsize=(10, 6))
sns.lmplot(data=df_tips, x='total_bill', y='tip', hue='sex', height=5, aspect=2)
plt.title('Total da conta vs. gorjeta (com regrressão)')

#Boxplot: Distribuição de gorjetas por dia da semana
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_tips, x='day', y='tip', palette='Set2')
plt.title("Gorjetas por dia da semana")

# gera o grafico em uma janela separada
plt.show()
