import requests
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def checkUserExistence(userEmail):
    response = requests.get('http://admin:admin@localhost:3000/api/users/lookup?loginOrEmail=' + userEmail)
        
    #check for http request code
    if response.status_code == 404:
        return False 
    else:
        return True

