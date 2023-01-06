# Description: Get Dashboard uid by Dashboard name
import logging
from scripts.dashboards.getAllDashboards import getAllDashboards
from scripts.dashboards.checkDashboardExistence import checkDashboardExistence

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getDashboardUid(dashboardName):
    if checkDashboardExistence(dashboardName) == False:
        logging.warning("getDashboardUid: Dashboard '%s' doesn't exist ❌", dashboardName)
        return None
    response = getAllDashboards()
    for dashboard in response:
        if dashboard["title"] == dashboardName:
            logging.info("getDashboardUid: Dashboard '%s' has id '%s' 👌", dashboard["title"], dashboard["uid"])
            return dashboard["uid"]
