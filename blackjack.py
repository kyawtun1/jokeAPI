import requests
import json
import pprint

dc = input("How many decks would you like?")

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=" + str(dc)

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

deckJson = response.json()

id = deckJson['deck_id']

print('Your deck ID is '+ str(id))
