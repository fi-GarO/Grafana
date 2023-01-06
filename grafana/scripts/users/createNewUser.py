import io
import json
import requests
import logging
from scripts.general.loadData import loadUserData
from scripts.users.checkUserExistence import checkUserExistence

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# Vstup file - cesta k souboru
def createNewUserFromFile(file):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }


    #solve UnicodeEncodeError: 'latin-1' codec can't encode character '\u0159' in position 16: ordinal not in range(256)
    with io.open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    response = requests.post('http://admin:admin@localhost:3000/api/admin/users', headers=headers, json=data)
    email = data['email']
    if checkUserExistence(email):
        logging.info("createNewUser: User '%s' already exists ❌", email)
        return False
    elif response.status_code == 200:
        logging.info("createNewUser: User '%s' successfully created 👌", data["email"])
        return True
    elif response.status_code == 400:
        logging.warning("createNewUser: bad request data from file '%s' ❌", file)
        return False

# Vstup je data z funkce loadUserData(file)
# Kontrolu je si sám existenci uživatele -> dostává userEmail (ne userId)
def createNewUser(data):
    if data == None:
        return False
    else:
        data = json.dumps(data)
        data = json.loads(data)
        for user in data:
            email = user['email']
            if checkUserExistence(email):
                logging.info("createNewUser: User '%s' already exists 👌", email)
            else:
                headers = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }
                response = requests.post('http://admin:admin@localhost:3000/api/admin/users', headers=headers, json=user)
                if response.status_code == 200:
                    logging.info("createNewUser: User '%s' successfully created 👌", user["email"])

    return True
