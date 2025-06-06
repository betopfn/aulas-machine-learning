# REGRESSÃO LINEAR
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Gerando dados simulados

X = 2.5 * np.random.rand(100, 1) * 100  # tamanho da casa
Y = 5000 * X + 10000 + np.random.randn(100, 1) * 20000  # Preço das casas

# Vizualizando a disrtribuição de dados
plt.scatter(X, Y)
plt.xlabel(X)
plt.ylabel(Y)
plt.title("Distribuição de preços por tamanho")


# Ajustando modelo de tregressão linear
model = LinearRegression()
model.fit(X, Y)

# Previsões e plotagem
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color="red")
plt.plot(X, model.predict(X), color="blue")
plt.title('Regressão Linear: Preço de Casa vs. Tamanho')
plt.xlabel('Tamanho (m²)')
plt.ylabel('Preço (R$)')
plt.show()