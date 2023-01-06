import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getFolderPermissions(folderUid):
    if folderUid is not None:
        headers = {
        "Accept": "application/json"
        }

        response = requests.get('http://admin:admin@localhost:3000/api/folders/' + folderUid + '/permissions', headers=headers)
        if response.status_code != 200:
            logging.error("getFolderPermissions: Error while loading folder permissions ❌")
            logging.error(response.text)
            return False

        response = json.loads(response.text)
        logging.info("getFolderPermissions: Folder permissions successfully loaded 👌")
        return response
    else:
        logging.error("getFolderPermissions: Folder not found ❌")
        return False