import requests
endpoint = 'http://localhost:8000/api/product/'
data={    'name': 'Pomme',
    'price': 10.99,
    'description': 'Une délicieuse pomme sucrée et juteuse.'}
response = requests.get(endpoint, json=data)
print(response.json())
print(response.status_code)