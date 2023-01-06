import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)


# True, když tým existuje. False, když tým neexistuje
def checkTeamExistence(teamName):
    response = requests.get('http://admin:admin@localhost:3000/api/teams/search?query=' + teamName)
    response = json.loads(response.text)
    if response["totalCount"] == 0:
        return False 
    else:
        return True
