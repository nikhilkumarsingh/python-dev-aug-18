import requests

url = "https://httpbin.org/ip"

r = requests.get(url)

print(r.json()['origin'])