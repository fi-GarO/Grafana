import requests
import json
import logging


logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getDashboardTitleByUid(dashboardUid):

    response = requests.get('http://admin:admin@localhost:3000/api/dashboards/uid/' + dashboardUid)
    if (response.status_code == 404):
        logging.warning("getDashboardTitleById: dashboard with uid '%s' doesn't exist ❌", dashboardUid)
        return None
    if (response.status_code == 401):
        logging.warning("getDashboardTitleById: Authentication error ❌")
        return None
    if (response.status_code == 403):
        logging.warning("getDashboardTitleById: Permission error ❌")
        return None
    if (response.status_code == 200):
        response = json.loads(response.text)
        logging.info("getDashboardTitleById: dashboard with uid '%s' has name '%s' 👌", dashboardUid, response["dashboard"]["title"])
        return response["dashboard"]["title"]

