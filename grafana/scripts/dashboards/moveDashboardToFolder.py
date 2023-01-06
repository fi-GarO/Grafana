
import logging
import requests
import json

from scripts.dashboards.getDashboardUid import getDashboardUid
from scripts.dashboards.getDashboardTitleByUid import getDashboardTitleByUid
from scripts.dashboards.getDashboardPanels import getDashboardPanels
from scripts.dashboards.checkIfDashboardIsInTheFolder import checkIfDashboardIsInTheFolder

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# Vstup dashboardUid a folderId
# Kontrola existence dashboardUid a folderId je v samotných funkcích getDashboardUid a getFolderId
def moveDashboardToFolder(dashboardUid, folderId):
    # Check if dashboard isn't in the folder
    if (checkIfDashboardIsInTheFolder(dashboardUid, folderId)):
        return True

    elif (checkIfDashboardIsInTheFolder(dashboardUid, folderId) == None):
        return False

    # Move dashboard to folder
    panels = getDashboardPanels(dashboardUid)    
    url = "http://admin:admin@localhost:3000/api/dashboards/db"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {
        "dashboard": {
            "title": getDashboardTitleByUid(dashboardUid),
            "uid": dashboardUid,
            "panels": panels
        },
        "folderId": folderId,
        "message": "Move dashboard to folder",
        "overwrite": True
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if (response.status_code == 200):
        logging.info("moveDashboardToFolder: Dashboard was moved 👌")
        return True
    if (response.status_code == 403):
        logging.warning("moveDashboardToFolder: Permission error ❌")
        return False
    if (response.status_code == 400):
        logging.warning("moveDashboardToFolder: Bad request ❌")
        return False
    if (response.status_code == 401):
        logging.warning("moveDashboardToFolder: Authentication error ❌")
        return False
    if (response.status_code == 412):
        logging.warning("moveDashboardToFolder: Precondition failed (dashboard with same name or uid already exists, version-mismatch, belongs to plugin) ❌")
        logging.warning("moveDashboardToFolder: Dashboard wasn't moved ❌")
        return False