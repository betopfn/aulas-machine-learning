from bs4 import BeautifulSoup
import requests
import pandas as pd

# Raspando dados do site Books to Scrape 
url = 'http://books.toscrape.com/'
reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')

# Extraindo nomes e preços de livros
produtos = soup.find_all('article', class_='product_pod')

for produto in produtos:
     nome = produto.find('h3').find('a')['title']
     preco = produto.find('p', class_='price_color').text
print(f"Nome: {nome}, Preço: {preco}")