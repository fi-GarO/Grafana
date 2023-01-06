# Description: Kontroluje, zda tým existuje
import logging

from scripts.folders.getAllFolders import getAllFolders

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)


# True, když tým existuje. False, když tým neexistuje
def checkFolderExistence(teamName):
    response = getAllFolders()
    for folder in response:
        if folder["title"] == teamName:
            return True
    return False
