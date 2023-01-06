import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getAllDashboards():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = requests.get('http://admin:admin@localhost:3000/api/search', headers=headers)

    if (response.status_code == 401):
        logging.warning("getAllDashboards: Authentication error ❌")
        return None
    if (response.status_code == 403):
        logging.warning("getAllDashboards: Permission error ❌")
        return None
    if (response.status_code == 200):
        response = json.loads(response.text)
        logging.info("getAllDashboards: dashboards successfully loaded 👌")
        return response

    return response.json()


