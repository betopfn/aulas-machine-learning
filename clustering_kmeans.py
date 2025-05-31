# Importando bibliotecas essenciais
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Configurando o ambiente para exibição de gráficos no notebook
#%matplotlib inline
sns.set(style='whitegrid')
pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

#selecione as festures numericas do database iris
#