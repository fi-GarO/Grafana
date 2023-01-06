import logging
import requests
import json
from scripts.dashboards.getDashboardTitleByUid import getDashboardTitleByUid

def checkIfDashboardIsInTheFolder(dashboardUid, folderId):
    if dashboardUid == None:
        logging.warning("checkIfDashboardIsInTheFolder: dashboardUid is None ❌")
        return None
    if folderId == None:
        logging.warning("checkIfDashboardIsInTheFolder: folderId is None ❌")
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
            if (response["meta"]["folderId"] == folderId):
                logging.info("checkIfDashboardIsInTheFolder: dashboard with uid: '%s' title: '%s' is already in folder with id: '%d' 👌", dashboardUid, getDashboardTitleByUid(dashboardUid), folderId)
                return True
            else:
                logging.info("checkIfDashboardIsInTheFolder: dashboard with uid: '%s' title: '%s' isn't in folder with id: '%d' 👌", dashboardUid, getDashboardTitleByUid(dashboardUid), folderId)
                return False