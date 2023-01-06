
import requests
import logging

from scripts.users.getUserId import getUserId
from scripts.users.getUserEmailById import getUserEmailById

from scripts.teams.getTeamId import getTeamId
from scripts.teams.getTeamNameById import getTeamNameById

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# Vstup userId a teamId
# Kontrola existence userId a teamId je v samotných funkcích getUserId a getTeamId
def addUserToTeam(userId, teamId):
    if userId == None:
        return False
    elif teamId == None:
        return False
    else:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = requests.post('http://admin:admin@localhost:3000/api/teams/' + str(teamId) + '/members/', headers=headers, json={"userId": userId})
        if response.status_code == 200:
            logging.info("addUserToTeam: User '%s' successfully added to team '%s' 👌", getUserEmailById(userId), getTeamNameById(teamId))
            return True
        elif response.status_code == 400:
            logging.info("addUserToTeam: User '%s' is already in team '%s' 👌", getUserEmailById(userId), getTeamNameById(teamId))
            return True
        else:
            logging.warning("addUserToTeam: User '%s' not added to team '%s' ❌, check status_code", getUserEmailById(userId), getTeamNameById(teamId))
            return False

    