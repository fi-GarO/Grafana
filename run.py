
import requests
import json
import io

def getAllUsers():
    headers = {
    "Accept": "application/json"
    }

    response = requests.get('http://admin:admin@localhost:3000/api/users')

    response = json.loads(response.text)
    return response

def createTeam(file):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    response = requests.post('http://admin:admin@localhost:3000/api/teams', headers=headers, data=open(file))
    return response


def getUserId(userName):
    response = requests.get('http://admin:admin@localhost:3000/api/users?query=' + userName)
    response = json.loads(response.text)
    userId = response[0]['id']
    return userId

def getTeamId(teamName):
    response = requests.get('http://admin:admin@localhost:3000/api/teams/search?query=' + teamName)
    response = json.loads(response.text)
    teamId = response["teams"][0]["id"]
    return teamId

def addUserToTeam(userId, teamId):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    response = requests.post('http://admin:admin@localhost:3000/api/teams/' + str(teamId) + '/members/', headers=headers, json={"userId": userId})
    return response.text

def createNewUser(file):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }


    #solve UnicodeEncodeError: 'latin-1' codec can't encode character '\u0159' in position 16: ordinal not in range(256)
    with io.open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    response = requests.post('http://admin:admin@localhost:3000/api/admin/users', headers=headers, json=data)
    return response.text

if __name__ == '__main__':
    #users = getAllUsers()
    #print(users)
    #print(createTeam('newTeam.json'))
    #userId = getUserId('jiri.turyna@jablotron.cz')
    #teamId = getTeamId('MyTestTeam')
    #addUserToTeam(userId, teamId)
    print(createNewUser('newUser.json'))
