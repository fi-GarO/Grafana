# Description: Get folder uid by folder name
import logging
from scripts.folders.getAllFolders import getAllFolders
from scripts.folders.checkFolderExistence import checkFolderExistence

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getFolderUid(teamName):
    if checkFolderExistence(teamName) == False:
        logging.warning("getFolderId: Folder '%s' doesn't exist ❌", teamName)
        return None
    response = getAllFolders()
    for folder in response:
        if folder["title"] == teamName:
            logging.info("getFolderId: Folder '%s' has uid '%s' 👌", folder["title"], folder["uid"])
            return folder["uid"]

