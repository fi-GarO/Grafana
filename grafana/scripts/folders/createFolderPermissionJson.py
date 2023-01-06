# Description: Create a JSON file with the permissions of a folder
import logging

logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)

def createFolderPermissionJson(response):
    if response != False:
        data = {
            "items": [
            ]
        }

        for item in response:
            # Jedná se o Admina -> lze skipnout, ten nelze editovat
            if item["permission"] == 4:
                pass
            elif "role" in item:
                # Jedná se o nějakou roli -> nechat mu práva jaký má
                data["items"].append({
                    "role": item["role"],
                    "permission": item["permission"]
                })
            # Jedná se o speciálního uživatele s nějakými právy -> nechat mu práva jaký má
            elif item["userEmail"] != "":
                data["items"].append({
                    "userId": item["userId"],
                    "permission": item["permission"]
                })
            # Jedná se o tým -> nechat jim práva jaký má
            else:
                data["items"].append({
                    "teamId": item["teamId"],
                    "permission": item["permission"]
                })

        return data

def createFolderPermissionEditorJson(response):
    data = {
        "items": [
        ]
    }

    for item in response:
        # Jedná se o Admina -> lze skipnout, ten nelze editovat
        if item["permission"] == 4:
            pass
        elif "role" in item:
            # Jedná se o Editora -> nastavit mu práva na 1
            if item["role"] == "Editor":
                data["items"].append({
                    "role": item["role"],
                    "permission": 1
                })
            else:
                # Jedná se o nějakou roli -> nechat mu práva jaký má
                data["items"].append({
                    "role": item["role"],
                    "permission": item["permission"]
                })
        # Jedná se o speciálního uživatele s nějakými právy -> nechat mu práva jaký má
        elif item["userEmail"] != "":
            data["items"].append({
                "userId": item["userId"],
                "permission": item["permission"]
            })
        # Jedná se o tým -> nechat jim práva jaký má
        else:
            data["items"].append({
                "teamId": item["teamId"],
                "permission": item["permission"]
            })

    return data