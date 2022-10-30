import requests

data = requests.get("https://regres.in/api/users")
print(f'{data.status_code}')
print(data.text)

