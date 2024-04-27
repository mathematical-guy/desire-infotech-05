import requests     # pip install requests

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/cricket"
result = requests.get(URL)

print(result)
print(result.json())