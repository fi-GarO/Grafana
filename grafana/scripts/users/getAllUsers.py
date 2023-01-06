import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getAllUsers():
    headers = {
    "Accept": "application/json"
    }

    response = requests.get('http://admin:admin@localhost:3000/api/users', headers=headers)

    response = json.loads(response.text)
    logging.info("getAllUsers: User data successfully loaded 👌")
    return response
