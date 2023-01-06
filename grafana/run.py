from scripts.teams.getTeamId import getTeamId
from scripts.teams.checkTeamExistence import checkTeamExistence 
from scripts.teams.createNewTeam import createNewTeam
from scripts.teams.getTeamNameById import getTeamNameById
from scripts.teams.createNewTeam import createNewTeamFromFile

from scripts.folders.getFolderUid import getFolderUid
from scripts.folders.checkFolderExistence import checkFolderExistence
from scripts.folders.createNewFolder import createNewFolder
from scripts.folders.getFolderTitleById import getFolderTitleById
from scripts.folders.getAllFolders import getAllFolders
from scripts.folders.getFolderPermissions import getFolderPermissions
from scripts.folders.createFolderPermissionJson import createFolderPermissionJson
from scripts.folders.setFolderPermissionsForTeam import setFolderPermissionsForTeam
from scripts.folders.getFolderId import getFolderId
from scripts.folders.getFolderUid import getFolderUid
from scripts.folders.checkFoldersPermissions import checkFoldersPermissions
from scripts.folders.setFolderPermissionsEditors import setFolderPermissionsEditors

from scripts.users.setDefaultUserPermissions import setDefaultUserPermissions
from scripts.users.getUserId import getUserId
from scripts.users.checkUserExistence import checkUserExistence
from scripts.users.createNewUser import createNewUser
from scripts.users.getUserEmailById import getUserEmailById
from scripts.users.addUserToTeam import addUserToTeam
from scripts.users.getAllUsers import getAllUsers
from scripts.users.getUserDataInOrganization import getUserDataInOrganization
from scripts.users.checkAllUserPermissions import checkAllUserPermissions

from scripts.general.loadData import loadUserData, loadTeamData

from scripts.dashboards.getDashboardUid import getDashboardUid
from scripts.dashboards.checkDashboardExistence import checkDashboardExistence
from scripts.dashboards.getDashboardUid import getDashboardUid
from scripts.dashboards.getAllDashboards import getAllDashboards
from scripts.dashboards.moveDashboardToFolder import moveDashboardToFolder
from scripts.dashboards.getDashboardVersions import getDashboardVersions
from scripts.dashboards.checkIfDashboardIsInTheFolder import checkIfDashboardIsInTheFolder
from scripts.dashboards.getDashboardPanels import getDashboardPanels
from scripts.dashboards.getDashboardPermissionsByUid import getDashboardPermissionsByUid
from scripts.dashboards.checkAllDashboardsAbilityToEdit import checkAllDashboardsAbilityToEdit
from scripts.dashboards.getInheritedPermissions import getInheritedPermissions



if __name__ == '__main__':
      
    # teams
    print("\nTeams")
    print("------------------")

    print("1. createNewTeam - loadData\n")
    file ='newTeams.json'
    file = '/home/jturyna/ops.tools/grafana/data/' + file
    createNewTeam(loadTeamData(file))
    print("...................")

    print("2. getTeamId\n")
    teamId = getTeamId('MyTestteam')
    print("...................")

    print("3. loadTeamData\n")
    teamFile ='newTeams.json'
    teamFile = '/home/jturyna/ops.tools/grafana/data/' + teamFile
    print("loadTeamData: " + str(loadTeamData(teamFile)))
    print("...................")

    # nějakej trouble u vytváření týmu z jsonu
    ##createNewTeamFromFile(file)

    print("4. getTeamNameById\n")
    teamName = getTeamNameById(3)
    print("...................")

    print("5. checkTeamExistence\n")
    print("checkTeamExistence: " + str(checkTeamExistence('team1')) + " 👌")


    # users
    print("\nUSERs")
    print("------------------")

    print("1. createNewUser\n")
    file ='newUser2.json'
    file = '/home/jturyna/ops.tools/grafana/data/' + file
    createNewUser(loadUserData(file))
    print("...................")

    print("2. createNewUser - multiple users\n")
    userFile ='newUsers.json'
    userFile = '/home/jturyna/ops.tools/grafana/data/' + userFile
    print("loadUserData: " + str(loadUserData(userFile)))
    print("...................")

    print("3. setDefaultUserPermissions\n")
    users = getUserDataInOrganization()
    setDefaultUserPermissions(users)
    print("...................")

    print("4. addUserToTeam\n")
    userId = getUserId('turyna@jablotron.cz')
    teamId = getTeamId('team1')
    addUserToTeam(userId, teamId)
    print("...................")

    print("5. checkUserExistence\n")
    print("checkUserExistence: " + str(checkUserExistence('jiri.turyna@jablotron.cz')) + " 👌")
    print("...................")

    print("6. getAllUsers\n")
    getAllUsers()
    print("...................")

    print("7. getUserEmailById\n")
    userEmail = getUserEmailById(1)
    print("...................")

    print("8. getUserDataInOrganization\n")
    getUserDataInOrganization()
    print("...................")

    print("9. checkAllUserPermissions\n")
    checkAllUserPermissions() 

    # folders
    print("\nFOLDERs")
    print("------------------")
 
    print("1. checkFolderExistence\n")
    print("checkFolderExistence: " + str(checkFolderExistence('team2')) + " 👌")
    print("...................")

    print("2. getFolderId\n")
    folderId = getFolderId('team2')
    print("...................")

    print("3. createNewFolder\n")
    createNewFolder('team2')
    print("...................")

    print("4. getFolderTitleById\n")
    folderTitle = getFolderTitleById(1)
    print("...................")

    print("5. getFolderUid\n")
    folderUid = getFolderUid('folder3')
    print("...................")

    print("6. getAllFolders\n")
    getAllFolders()
    print("...................")

    print("7. getTeamId\n")
    teamId = getTeamId('team2')
    print("...................")

    print("8. setFolderPermissionsForTeam\n")
    setFolderPermissionsForTeam(folderUid, teamId)
    print("...................")

    print("9. createFolderPermissionJson\n")
    createFolderPermissionJson(getFolderPermissions(folderUid))
    print("...................")
 

    print("10. checkFoldersPermissions\n")
    checkFoldersPermissions()
    print("...................")


    print("11. setFolderPermissionsEditors\n")
    setFolderPermissionsEditors()
 
    # dashboards
    print("\nDASHBOARDs")
    print("------------------")

    print("1. checkDashboardExistence\n")
    print("checkDashboardExistence: " + str(checkDashboardExistence('New dashboard')) + " 👌")
    print("...................")

    # Nedává smysl - dashboardUid nelze hledat podle názvu, mohou být duplikáty
    print("2. getDashboardUid\n")
    dashboardUid = getDashboardUid('New dashboard')
    print("...................")


    print("3. getAllDashboards\n")
    getAllDashboards()
    print("...................")


    print("4. moveDashboardToFolder\n")
    dashboardUid = "1PzBT2cVz"
    folderId = getFolderId('team2')
    moveDashboardToFolder(dashboardUid, folderId)
    print("...................")

    print("5. getDashboardVersions\n")
    dashboardUid = "1PzBT2cVz"
    getDashboardVersions(dashboardUid)
    print("...................")


    print("6. checkIfDashboardIsInTheFolder\n")
    dashboardUid = "1PzBT2cVz"
    folderId = getFolderId('team2')
    checkIfDashboardIsInTheFolder(dashboardUid, folderId)
    print("...................")


    print("7. getDashboardPanels\n")
    dashboardUid = "1PzBT2cVz"
    getDashboardPanels(dashboardUid)
    print("...................")  

    print("8. getDashboardPermissionsByUid\n")
    dashboardUid = "1PzBT2cVz"
    getDashboardPermissionsByUid(dashboardUid)
    print("...................")

    print("9. getInheritedPermissions\n")
    dashboardUid = "1PzBT2cVz"
    getInheritedPermissions(dashboardUid)
    print("...................")

    print("10. checkAllDashboardsAbilityToEdit\n")
    dashboards = getAllDashboards()
    checkAllDashboardsAbilityToEdit(dashboards)










