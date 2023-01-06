import requests
import json
import logging
from scripts.folders.getAllFolders import getAllFolders

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def checkFoldersPermissions():
    data = getAllFolders()
    for folder in data:

        url = "http://admin:admin@localhost:3000/api/folders/" + folder["uid"] + "/permissions"
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            logging.error("checkFoldersPermissions: Error while getting permissions for folder uid:'%s' title: '%s' ❌", folder["uid"], folder["title"])
            logging.error(response.text)
            return False

        response = json.loads(response.text)
        for permission in response:
            if "role" in permission:
                if permission["role"] == "Editor" and permission["permission"] == 2:
                    logging.error("checkFoldersPermissions: Editor permissions for folder uid:'%s' title: '%s' are not OK ❌", folder["uid"], folder["title"])
                    return False            
                elif permission["role"] == "Viewer" and permission["permission"] != 1:
                    logging.warning("checkFoldersPermissions: Viewer Permissions for folder uid:'%s' title: '%s' do not equal 'VIEW' ❌ - check if intended", folder["uid"], folder["title"])
        logging.info("checkFoldersPermissions: Permissions for folder uid:'%s' title: '%s' are OK 👌", folder["uid"], folder["title"])    
    return True

if __name__ == "__main__":
    checkFoldersPermissions()