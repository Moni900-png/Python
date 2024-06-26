import requests


url = 'https://reqres.in/api/users'

payload = {
    'name': 'morpheus',
    'job': 'leader'
}
response = requests.post(url, json=payload)
if response.status_code == 200:
    print('Response JSON:', response.json())
else:
    print('Status code:', response.status_code)