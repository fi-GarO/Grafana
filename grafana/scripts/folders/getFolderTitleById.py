import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getFolderTitleById(folderId):

    response = requests.get('http://admin:admin@localhost:3000/api/folders/id/' + str(folderId))
    if (response.status_code == 404):
        logging.warning("getFolderTitleById: Folder with id '%d' doesn't exist ❌", folderId)
        return None
    if (response.status_code == 401):
        logging.warning("getFolderTitleById: Authentication error ❌")
        return None
    if (response.status_code == 403):
        logging.warning("getFolderTitleById: Permission error ❌")
        return None
    if (response.status_code == 200):
        response = json.loads(response.text)
        logging.info("getFolderTitleById: Folder with id '%d' has name '%s' 👌", folderId, response["title"])
        return response["title"]

