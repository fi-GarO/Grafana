import json
import requests
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# get team name by id 
def getTeamNameById(teamId):
    response = requests.get('http://admin:admin@localhost:3000/api/teams/' + str(teamId))
    if response.status_code == 404:
        logging.warning("getTeamNameById: Team with id '%d' doesn't exist ❌", teamId)
        return None
    else:
        response = json.loads(response.text)
        teamName = response['name']
        logging.info("getTeamNameById: Team with id '%d' has name '%s' 👌", teamId, teamName)
    return teamName
