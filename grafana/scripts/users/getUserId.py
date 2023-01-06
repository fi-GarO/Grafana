from scripts.users.checkUserExistence import checkUserExistence
import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def getUserId(userEmail):
    if checkUserExistence(userEmail) == False:
        logging.warning("getTeamId: User '%s' doesn't exist ❌", userEmail)
        return None
    else:
        response = requests.get('http://admin:admin@localhost:3000/api/users/lookup?loginOrEmail=' + userEmail)
        response = json.loads(response.text)
        userId = response['id']
        logging.info("getTeamId: User '%s' has id '%d' 👌", userEmail, userId)
        return userId

