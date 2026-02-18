import requests
endpoint = 'http://localhost:8000/api/'
data={    'name': 'Avocat',
    'price': 10.99,
    'description': 'Une délicieuse mangue sucrée et juteuse.'}
response = requests.get(endpoint)
print(response.json())
print(response.status_code)