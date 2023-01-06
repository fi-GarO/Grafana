# Description: Creates new folder in Grafana
import requests
import logging

from scripts.teams.checkTeamExistence import checkTeamExistence
from scripts.folders.checkFolderExistence import checkFolderExistence
logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)


# Vstup teamName
# Provádí si sama kontrolu, zda-li tým existuje, protože se jí předává teamName (a ne teamId)
def createNewFolder(teamName):
    # team existuje
    if checkTeamExistence(teamName) == False and checkFolderExistence(teamName) == False or checkTeamExistence(teamName) == True and checkFolderExistence(teamName) == False:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = requests.post('http://admin:admin@localhost:3000/api/folders', headers=headers, data='{"title": "' + teamName + '"}')
        if response.status_code == 200:
            logging.info("createNewFolder: Folder " + teamName + " successfully created 👌")
            return True
        else:
            logging.info("createNewFolder: Folder " + teamName + " was not created ❌")
            return False
    else:
        logging.info("createNewFolder: Folder " + teamName + " already exists 👌")
        return False
