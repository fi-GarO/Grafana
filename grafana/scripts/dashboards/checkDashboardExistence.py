# Description: Kontroluje, zda dashboard existuje
import logging

from scripts.dashboards.getAllDashboards import getAllDashboards

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# True, když dashboard existuje. False, když dashboard neexistuje
def checkDashboardExistence(dashboardName):
    response = getAllDashboards()
    for dashboard in response:
        if "folderUid" in dashboard:
            if dashboard["title"] == dashboardName:
                return True
    return False

