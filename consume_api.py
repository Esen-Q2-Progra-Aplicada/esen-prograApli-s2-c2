# client
import requests

response = requests.put("http://127.0.0.1:5000/helloworld/sofia/32/1800.5")
print(response)
messageJson = response.json()
print(messageJson)
if response.status_code == 200:
    messageJson = response.json()
    print(messageJson["name"], messageJson["age"], messageJson["salary"])
