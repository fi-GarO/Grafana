import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def setDefaultUserPermissions(users):
    for user in users:
        if user["role"] == "Editor":
            logging.info("setDefaultUserPermissions: user '%s' is an edior 👌", user["login"])
            continue
        if user["role"] == "Admin":
            logging.info("setDefaultUserPermissions: user '%s' is an admin 👌", user["login"])
            continue
        else:
            logging.info("setDefaultUserPermissions: user '%s' is not an ❌", user["login"])
            response = requests.patch("http://admin:admin@localhost:3000/api/org/users/" + str(user["userId"]), json={"role": "Editor"})
            if response.status_code == 200:
                logging.info("setDefaultUserPermissions: user '%s' is now an editor 👌", user["login"])
            else:
                logging.error("setDefaultUserPermissions: response is '%s' ❌", response.text)