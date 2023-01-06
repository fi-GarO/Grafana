import requests
import json
import logging

from scripts.dashboards.checkDashboardExistence import checkDashboardExistence
from scripts.dashboards.getDashboardPermissionsByUid import getDashboardPermissionsByUid
from scripts.dashboards.getInheritedPermissions import getInheritedPermissions

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)


def checkAllDashboardsAbilityToEdit(dashboards):
    if dashboards is None:
        logging.error("checkAllDashboardAbilityToEdit: dashboards not loaded ❌")
        return False
    if dashboards is None:
        logging.error("checkAllDashboardAbilityToEdit: dashboards not loaded ❌")
        return False
    notEditableDashboards = []
    for dashboard in dashboards:
        if checkDashboardExistence(dashboard["title"]):
            dashboardPermissions = getDashboardPermissionsByUid(dashboard["uid"]) 
            if "folderId" in dashboard:
                dashboardPermissions.extend(getInheritedPermissions(dashboard["folderId"]))        
            if 2 in dashboardPermissions:
                logging.warning("checkAllDashboardAbilityToEdit: dashboard '%s' is editable 👌", dashboard["title"])
            else:
                notEditableDashboards.append(dashboard["uid"])
                logging.info("checkAllDashboardAbilityToEdit: dashboard '%s' is not editable ❌", dashboard["title"])
    if len(notEditableDashboards) > 0:
        logging.error("checkAllDashboardAbilityToEdit: dashboards '%s' are not editable ❌", notEditableDashboards)
        return False
    else:
        logging.info("checkAllDashboardAbilityToEdit: all dashboards are editable 👌")  
    return True
