from bs4 import BeautifulSoup
import requests

# Raspando dados do site de noticias

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraindo Titulo da noticias
autores = [tag.text for tag in soup.find_all('a', class_='hnuser')]
for i, autor in enumerate(autores, 1):
    print(f"Autor {i}: {autor}")

