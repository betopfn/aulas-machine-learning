from bs4 import BeautifulSoup
import requests
import pandas as pd

# Url da Spacex para espaço-naves

url = 'https://api.spacexdata.com/v4/dragons'
response = requests.get(url)
data = response.json()

# criando listas para armazenar informaçoes sobre as espaçonaves
nomes = []
tipos = []
massas = []
capacidades = []

for dragon in data:
        nomes.append(dragon['name'])
        tipos.append(dragon['type'])
        massas.append(dragon['dry_mass_kg'])
        capacidades.append(dragon['launch_payload_mass']['kg'])

# Criando um DataFrame com os dados coletados
df_dragons = pd.DataFrame({
    'Nome': nomes,
    'Tipo': tipos,
    'Massa Seca (kg)': massas,
    'Capacidade de Lançamento (kg)': capacidades
})

print(df_dragons)
