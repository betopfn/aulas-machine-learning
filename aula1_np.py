import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# gera o grafico em uma janela separada
plt.show()

sns.set(style='whitegrid')

pd.set_option('display.max_columns', None)

print("Ambiente configurado e bibliotecas importadas!")

#criando uma array unidimensional
lista1 = [10, 20, 30, 40, 50, 60, 70, 80]

arr = np.array(lista1)

print("array unidimensional", arr)

#operações com a array
#soma
print("a soma de todos os numeros da lista é: ", arr.sum())
#media
print("a media é: ", arr.mean())
#
print("multiplicand a lsta por 2", arr * 2)

## Criando um array bidimensional (matriz)
matriz = np.array([[10, 20, 30, 40], 
                    [50, 60, 70, 80]])
print("matriz: ", matriz)

# Indexação e slicing
print("Elemento coluna 2, linha 1:", matriz[0,1])
print("Slicing linha 2:",  matriz[1,0:3])

# Somando um vetor a cada linha da matriz
vetor = np.array([1, 2, 3, 4])
resultado = matriz + vetor
print("resultado do broadcast: (matriz + vetor)")
print(resultado)

# Multiplicação de matrizes

A = np.array([[1, 2], 
                [3, 4]])
B = np.array([[5, 6], 
                [7, 8]])

produto = np.dot(A, B)
print("a matriz A x B, da a matriz:", produto)

# Funções matemáticas
array_exemplo = np.array([1, 2, 3, 4, 5])
# sempre eleva ao e, e = numero de euler = ≈2.71828
print("\nExponenciação:", np.exp(array_exemplo))
print("Logaritmo natural:", np.log(array_exemplo))