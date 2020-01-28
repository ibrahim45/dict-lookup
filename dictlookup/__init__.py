import os 
import requests
import pprint

API_TOKEN = os.environ.get('API_TOKEN', None)
OWL_URI = 'https://owlbot.info/api/v4/dictionary/'
if API_TOKEN is None:
    print("Please enter the OWL dictionaries API token by following steps in readme.md")
    exit()


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