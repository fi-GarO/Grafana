from scripts.teams.checkTeamExistence import checkTeamExistence 
import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)


def getTeamId(teamName):
    if checkTeamExistence(teamName) == False:
        logging.warning("getTeamId: Team '%s' doesn't exist 👌", teamName)
        return None
    else:
        response = requests.get('http://admin:admin@localhost:3000/api/teams/search?query=' + teamName)
        response = json.loads(response.text)
        teamId = response['teams'][0]['id']
        logging.info("getTeamId: Team '%s' has id '%s' 👌", teamName, teamId)
        return teamId


