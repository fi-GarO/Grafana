import requests
import json
import sys
import logging

from scripts.dashboards.getDashboardTitleByUid import getDashboardTitleByUid

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getDashboardPermissionsByUid(dashboardUid):
    if dashboardUid is None:
        logging.warning("getDashboardPermissionsByUid: dashboardUid is None ❌")
        return None

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = requests.get('http://admin:admin@localhost:3000/api/dashboards/uid/' + dashboardUid + '/permissions', headers=headers)
 
    if (response.status_code == 401):
        logging.warning("getDashboardPermissionsByUid: Authentication error ❌")
        return None
    if (response.status_code == 403):
        logging.warning("getDashboardPermissionsByUid: Permission error ❌")
        return None
    if (response.status_code == 404):
        logging.warning("getDashboardPermissionsByUid: dashboard with uid '%s' doesn't exist ❌", dashboardUid)
        return None
    if (response.status_code == 200):
        listOfPermissions = []
        permissions = json.loads(response.text)
        for permission in permissions:
            listOfPermissions.append(permission["permission"])
        logging.info("getDashboardPermissionsByUid: dashboard with uid '%s' title '%s' has permissions '%s' 👌", dashboardUid, getDashboardTitleByUid(dashboardUid), listOfPermissions)
        return listOfPermissions

    return None

    