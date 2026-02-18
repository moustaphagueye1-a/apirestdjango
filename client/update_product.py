import requests
endpoint = 'http://localhost:8000/api/product/1/'
data={    'name': 'Papaye',
    'price': 10.99,
    'description': 'Une délicieuse papaye sucrée et juteuse.'}
response = requests.put(endpoint, json=data)
print(response.json())
print(response.status_code)