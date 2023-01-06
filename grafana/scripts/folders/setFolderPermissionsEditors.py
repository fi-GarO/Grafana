import requests
import json
import logging

from scripts.folders.createFolderPermissionJson import createFolderPermissionEditorJson
from scripts.folders.getFolderPermissions import getFolderPermissions
from scripts.folders.checkFoldersPermissions import checkFoldersPermissions
from scripts.folders.getAllFolders import getAllFolders

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# folderUid i teamId si svoji existenci ověřují přímo v těchto funkcích
# True pokuď všechny složky mají nastavené oprávnění pro editory na 1, False pokud ne
def setFolderPermissionsEditors():
    if checkFoldersPermissions():
        logging.info("setFolderPermissionsEditors: Permissions for all folders are OK 👌")
        return True    
    else:
        logging.error("setFolderPermissionsEditors: Permissions for Editors are not OK... changing 👌")

        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        folders = getAllFolders()
        for folder in folders:
            data = createFolderPermissionEditorJson(getFolderPermissions(folder["uid"]))
            response = requests.post('http://admin:admin@localhost:3000/api/folders/' + folder["uid"] + '/permissions', headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                logging.info("setFolderPermissionsEditors: Folder permissions successfully set for folder uid:'%s' title: '%s'👌", folder["uid"], folder["title"])
                response = json.loads(response.text)

            else:
                logging.error("setFolderPermissionsEditors: Folder permissions couldn't be set for folder uid:'%s' title: '%s' ❌", folder["uid"], folder["title"])
                response = json.loads(response.text)
                logging.error(response)
                return False
        return True
        
  
