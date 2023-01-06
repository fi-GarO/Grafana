import requests
import json
import logging

from scripts.folders.createFolderPermissionJson import createFolderPermissionJson
from scripts.folders.getFolderPermissions import getFolderPermissions

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# folderUid i teamId si svoji existenci ověřují přímo v těchto funkcích
def setFolderPermissionsForTeam(folderUid, teamId):
    if folderUid is None:
        logging.error("setFolderPermissionsForTeam: Folder not found ❌")
        return False
    elif teamId is None:
        logging.error("setFolderPermissionsForTeam: Team not found ❌")
        return False
    else:
        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        data = createFolderPermissionJson(getFolderPermissions(folderUid))
        data["items"].append({
            "teamId": teamId,
            "permission": 2
        })
        
        response = requests.post('http://admin:admin@localhost:3000/api/folders/' + folderUid + '/permissions', headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            logging.info("setFolderPermissionsForTeam: Folder permissions successfully set 👌")
            response = json.loads(response.text)
            return response

        else:
            logging.error("setFolderPermissionsForTeam: Folder permissions couldn't be set ❌")
            response = json.loads(response.text)
            logging.error(response)
            return response

