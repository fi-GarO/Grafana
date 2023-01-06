# Description: Get folder uid by folder id
import logging
from scripts.folders.getAllFolders import getAllFolders
logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getFolderUidById(folderId):
    response = getAllFolders()
    for folder in response:
        if folder["id"] == folderId:
            logging.info("getFolderUidById: Folder '%s' has uid '%s' 👌", folder["title"], folder["uid"])
            return folder["uid"]
