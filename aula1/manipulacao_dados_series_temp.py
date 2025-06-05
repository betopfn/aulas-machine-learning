import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




sns.set(style='whitegrid')

pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

# Criação de uma serie temporal com date_range
datas = pd.date_range(start='2024-01-01', periods=10, freq='ME')

#Crianddo um DataFrame com dados de vendas diárias simuladas
df_temporal = pd.DataFrame({
    'Data': datas,
    'Vendas': np.random.randint(100, 500, size=10)
})
df_temporal.set_index('Data', inplace=True)
print("\n DataFrame com série temporal:")


# Resampling: média de vendas a cada 3 dias
df_resampled = df_temporal.resample('3D').mean()
print("\nDataFrame reamostrado(média a cada 3 dias)")
print(df_resampled)