import requests

# consumindo API para obter dados

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
dados = response.json()
print(dados)