import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getDashboardPanels(dashboardUid):
    if dashboardUid == None:
        logging.warning("getDashboardPanels: dashboardUid is None ❌")
        return None
    else:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = requests.get('http://admin:admin@localhost:3000/api/dashboards/uid/' + dashboardUid, headers=headers)
        if (response.status_code == 404):
            logging.warning("getDashboardPanels: dashboard with uid '%s' doesn't exist ❌", dashboardUid)
            return None
        if (response.status_code == 401):
            logging.warning("getDashboardPanels: Authentication error ❌")
            return None
        if (response.status_code == 403):
            logging.warning("getDashboardPanels: Permission error ❌")
            return None
        if (response.status_code == 200):
            response = json.loads(response.text)
            logging.info("getDashboardPanels: Successfully loaded panels data for dashboard '%s' 👌", dashboardUid)
            return response["dashboard"]["panels"]

        return response.json()

