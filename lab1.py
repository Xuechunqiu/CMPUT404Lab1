import requests

print(requests.__version__)

url = "http://www.google.com/"
response = requests.get(url)
print(response.status_code)