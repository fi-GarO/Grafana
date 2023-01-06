import logging

from scripts.dashboards.getDashboardPermissionsByUid import getDashboardPermissionsByUid
from scripts.folders.getFolderUidById import getFolderUidById
from scripts.folders.getFolderPermissions import getFolderPermissions

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getInheritedPermissions(folderId):
    inheritedPermissions = []
    if folderId is None:
        logging.warning("getInheritedPermissions: folderId is None ❌")
        return None
    folderUid = getFolderUidById(folderId)
    if folderUid is None:
        logging.warning("getInheritedPermissions: folderUid is None ❌")
        return None
    response = getFolderPermissions(folderUid)
    if response is None:
        logging.warning("getInheritedPermissions: response is None ❌")
        return None
    for data in response:
        inheritedPermissions.append(data["permission"])

    logging.info("getInheritedPermissions: Inherited permissions for folder with id '%d' are '%s' 👌", folderId, inheritedPermissions)
    
    return inheritedPermissions   
