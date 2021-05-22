# client
import requests

response = requests.post("http://127.0.0.1:5000/helloworld")
print(response)
messageJson = response.json()
print(messageJson)
if response.status_code == 200:
    messageJson = response.json()
    print(messageJson["data"])
