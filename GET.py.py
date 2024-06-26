import requests

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')