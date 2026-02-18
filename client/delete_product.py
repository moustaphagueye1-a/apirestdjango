import requests

endpoint = 'http://localhost:8000/api/product/3/'

response = requests.delete(endpoint)

print("Status code:", response.status_code)

if response.status_code == 204:
    print("Produit supprimé avec succès")
else:
    print(response.text)
