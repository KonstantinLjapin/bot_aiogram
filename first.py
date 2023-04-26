import requests

url = ""
response = requests.get("http://numbersapi.com/43")
print(response.text)
