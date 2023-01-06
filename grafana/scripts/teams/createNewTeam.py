import json
import requests
import logging
from scripts.general.loadData import loadTeamData
from scripts.teams.checkTeamExistence import checkTeamExistence

# vstup file
def createNewTeamFromFile(file):
    #open file with team data and print it
    with open(file) as f:
        data = json.load(f)

    #exception if json parameter not found
    try:
        teamName=data["name"]
    except KeyError:
        logging.warning("createNewTeam: Not valid json file '%s' parameter 'name' not found 👌", file)
        return False

    if checkTeamExistence(teamName) == False:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

        response = requests.post('http://admin:admin@localhost:3000/api/teams', headers=headers, data=open(file))

    else:
        logging.warning("createNewTeam: Team '%s' already exists 👌", teamName)
        return False

    logging.info("createNewTeam: Team '%s' successfully created 👌", teamName)
    return True

def createNewTeam(data):
    if data == None:
        return False
    else:
        data = json.dumps(data)
        data = json.loads(data)
    
        for team in data:
            teamName = team["name"]
            if checkTeamExistence(teamName) == False:
                headers = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                response = requests.post('http://admin:admin@localhost:3000/api/teams', headers=headers, json=team)
                if response.status_code == 200:
                    logging.info("createNewTeam: Team '%s' successfully created 👌", team["name"])

            else:
                logging.warning("createNewTeam: Team '%s' already exists 👌", teamName)
    return True
