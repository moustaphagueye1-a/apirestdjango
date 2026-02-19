import requests
endpoint = 'http://localhost:8000/api/product/'
data={    'name': 'Cerise',
    'price': 10.99,
    'description': 'Une délicieuse cerise sucrée et juteuse.'}
response = requests.post(endpoint, json=data)
print(response.json())
print(response.status_code)