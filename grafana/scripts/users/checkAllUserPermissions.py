import logging
from scripts.users.getUserDataInOrganization import getUserDataInOrganization

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

# Check if all users have correct permissions - only one admin, no editors, everyone is viewer
def checkAllUserPermissions():
    admins = []
    editors = []
    viewers = []
    data = getUserDataInOrganization()
    if data == None:
        return False
    else:
        for user in data:
            if user['role'] == 'Admin':
                admins.append(user['email'])              
            elif user['role'] == 'Editor':
                editors.append(user['email'])
            elif user['role'] == 'Viewer':
                viewers.append(user['email'])
            else:
                logging.warning("checkAllUserPermissions: User '%s' has unknown role ❌", user['email'])
                return False
        if len(admins) != 1:
            logging.warning("checkAllUserPermissions: There is more than one admin! ❌")
            print("Admins: ", admins)
            return False
        if len(editors) == 0:
            logging.warning("checkAllUserPermissions: There is no editor! ❌")
            print("Editors: ", editors)
            return False
        if len(viewers) != 0:
            logging.warning("checkAllUserPermissions: There is a viewer! ❌")
            return False
   
        logging.info("checkAllUserPermissions: All users have correct permissions 👌")
        return True
