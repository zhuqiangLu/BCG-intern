import requests
import json
import CONFIG

uri = CONFIG.BASE_URI + CONFIG.KEY_ENDPOINT
#the uri is not trusted
step1 = requests.get(uri, verify = False, headers=CONFIG.HEADER)
print(step1.status_code) #to make sure it is 201
key = step1.json()["key"]

submitURI = CONFIG.BASE_URI + CONFIG.SUBMIT_ENDPOINT + key
payload = json.loads(CONFIG.APPLICATION)
step2 = requests.post(submitURI, json = payload, headers = CONFIG.HEADER)
print(step2.status_code)
print(step2.json()) 

