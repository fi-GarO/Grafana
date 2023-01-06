
import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getDashboardVersions(dashboardUid):
    if dashboardUid == None:
        logging.warning("getDashboardVersions: dashboardUid is None ❌")
        return None
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = requests.get('http://admin:admin@localhost:3000/api/dashboards/uid/' + dashboardUid + '/versions', headers=headers)
    logging.info("getDashboardVersions: dashboardVersions successfully loaded 👌")
    return response.json()

