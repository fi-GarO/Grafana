import json
import requests
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# get user email by id
# TODO - check for fail response
def getUserEmailById(userId):
    response = requests.get('http://admin:admin@localhost:3000/api/users/' + str(userId))
    response = json.loads(response.text)
    userEmail = response['email']
    logging.info("getUserEmailById: User with id '%d' has email '%s' 👌", userId, userEmail)
    return userEmail
