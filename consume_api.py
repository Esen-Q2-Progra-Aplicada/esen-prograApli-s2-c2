# client
import requests

response = requests.get("http://127.0.0.1:5000/helloworld")
print(response)
if response.status_code == 200:
    messageJson = response.json()
    print(messageJson["data"])