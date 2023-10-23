import requests as api

response = api.get(url='http://api.open-notify.org/iss-now.json')
print(response)
