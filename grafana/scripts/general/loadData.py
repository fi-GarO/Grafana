import json
import logging
import os.path

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def loadUserData(file):
    listOfData = []
    if os.path.isfile(file) == False:
        logging.warning("loadUserData: File '%s' doesn't exist ❌", file)
        return None
    with open(file, 'r') as f:
        data = json.load(f)
        for user in data:
            listOfData.append(user)
        if validateUserData(listOfData) == True:
            return listOfData
        else:
            return None

def loadTeamData(file):
    listOfTeamData = []
    if os.path.isfile(file) == False:
        logging.warning("loadTeamData: File '%s' doesn't exist ❌", file)
        return None
    with open(file, 'r') as f:
        data = json.load(f)
        for team in data:
            listOfTeamData.append(team)
        if validateTeamData(listOfTeamData) == True:
            return listOfTeamData
        else:
            return None

def validateTeamData(listOfData):
    parameters = ["name"]
    for team in listOfData:
        try:
            for parameter in parameters:
                if team[parameter] == "":
                    logging.warning("validateTeamData: Not valid json file - parameter '%s' is empty ❌", parameter)
                    return False
        except KeyError:
            logging.warning("validateTeamData: Not valid json file - missing some of required parameters %s ❌", parameters)
            return False
    return True

def validateUserData(listOfData):
    parameters = ["name", "email", "login", "password"]
    for user in listOfData:
        try:
            for parameter in parameters:
                if user[parameter] == "":
                    logging.warning("validateUserData: Not valid json file - parameter '%s' is empty ❌", parameter)
                    return False
        except KeyError:
            logging.warning("validateUserData: Not valid json file - missing some of required parameters %s ❌", parameters)
            return False
    return True
