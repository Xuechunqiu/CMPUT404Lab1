import requests

print(requests.__version__)

url = "http://www.google.com/"
response = requests.get(url)
print(response.status_code)

url_itself = "https://raw.githubusercontent.com/Xuechunqiu/CMPUT404Lab1/master/lab1.py"
response = requests.get(url_itself)
print(response.text)