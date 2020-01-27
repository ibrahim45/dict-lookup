import os 
import requests
import pprint

API_TOKEN = os.environ.get('API_TOKEN')
print(API_TOKEN)
OWL_URI = 'https://owlbot.info/api/v4/dictionary/'
token = 'Token  ' + API_TOKEN
pp = pprint.PrettyPrinter(indent=4)


def search_word(word):
    headers = {
        'Authorization': token
    }
    url = OWL_URI + word.strip()
    response = requests.get(url, headers=headers)
    pp.pprint(response.json())
    return 
