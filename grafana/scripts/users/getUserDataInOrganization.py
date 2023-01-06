import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)


def getUserDataInOrganization():
    headers = {
    "Accept": "application/json"
    }
    response = requests.get('http://admin:admin@localhost:3000/api/orgs/1/users', headers=headers)
    if response.status_code != 200:
        logging.error("getUserDataInOrganization: Error while loading user data ❌")
        return None
    response = json.loads(response.text)
    logging.info("getUserDataInOrganization: User data successfully loaded 👌")

    return response

