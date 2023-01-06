from scripts.teams.getTeamId import getTeamId
from scripts.teams.checkTeamExistence import checkTeamExistence 
from scripts.teams.createNewTeam import createNewTeam
from scripts.teams.getTeamNameById import getTeamNameById
from scripts.teams.createNewTeam import createNewTeamFromFile

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
from scripts.folders.getFolderUidById import getFolderUidById

from scripts.users.getUserId import getUserId
from scripts.users.checkUserExistence import checkUserExistence
from scripts.users.createNewUser import createNewUser
from scripts.users.createNewUser import createNewUserFromFile
from scripts.users.getUserEmailById import getUserEmailById
from scripts.users.addUserToTeam import addUserToTeam
from scripts.users.getAllUsers import getAllUsers
from scripts.users.getUserDataInOrganization import getUserDataInOrganization
from scripts.users.checkAllUserPermissions import checkAllUserPermissions
from scripts.users.setDefaultUserPermissions import setDefaultUserPermissions

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
from scripts.dashboards.getInheritedPermissions import getInheritedPermissions
from scripts.dashboards.checkAllDashboardsAbilityToEdit import checkAllDashboardsAbilityToEdit

if __name__ == '__main__':
    checkAllDashboardsAbilityToEdit(getAllDashboards())
    #getDashboardPermissionsByUid('QP6_ERhVk')
    #getFolderTitleById(8)
    #setDefaultUserPermissions(getUserDataInOrganization())
