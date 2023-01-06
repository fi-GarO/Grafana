# Description: Get all folders in Grafana
import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# limit is 1000 folders by default
def getAllFolders():
    headers = {
    "Accept": "application/json"
    }

    response = requests.get('http://admin:admin@localhost:3000/api/folders', headers=headers)

    response = json.loads(response.text)
    logging.info("getAllFolders: Folder data successfully loaded 👌")
    return response
