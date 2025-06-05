import bs4
import requests

# consumido API de cotação de moedas
url = 'https://api.exchangerate-api.com/v4/latest/USD'
response = requests.get(url)
exchange_data = response.json()

# Exibindo cotação do dólar para o euro
dolar_to_euro = exchange_data['rates']['EUR']
print(f"1 Dólar vale {dolar_to_euro} Euros")