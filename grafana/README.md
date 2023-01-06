# Grafana
# Connect ELK-PRD1
- VPN
@192.168.24.204

# Todo

- getDashboardUid -> předělat -> aktuálně nefunguje na duplikáty (může být víc dashboardů se stejným jménem napříč složkami, ale né v jedné složce)
    - Přidat kontext folderId, aby bylo jasné který board je na mysli. 
    - moveDashboard to Folder + otestovat jak se bude chovat, když přesuneš board se stejným jménem -> odchytit
    - dashboardExistence
    - getDashboardUid 

- Rozšířit vstupní JSON o možnost role -> není funkční pro Grafana API a je potřeba napsat změnu pro PATCH
        - Chceme umět, aby sice byl každý Editor, ale pokud je definováno v Jsonu -> bude mu ponechán Viewer 
            - Potřeba přidat parametr "role" do JSON validace

- getUserEmailById - check for fail response

- getData one time na vstupu a passovat jako argument místo volat getAll...() při každém callu funkce



- Otestovat co budou dashboardy dělat, když budou v General složce - minimálně checkAllDashboardAbilityToEdit -> tahá si z jsonu folderId a nevim co to udělá pro General 
    - nedává folderId
    - dodělat, když nemá folderId -> getDashboardPermission -> a viewer nemá edit -> nejde editovat (všichni jsou viewer) 
        - Všichni jsou už EDITOR (setDefaultUserPermissions) - DONE
- zapřemýšlet jestli by nedávalo smysl mít všechny jako Editor -> když vytvořím dashboard v General, můžu ho hned editovat a zároveň všude jinde mám furt jen view
    - DONE
- create user permissions = Viewer - DONE
- bere Json:
    - addUserToTeam -> vezmu json, projdu všechny emaily a team parametry a přidám uživatele do týmu - DONE
        - Podle mě nedává smysl, aby bral JSON. Něco jinýho bude rozebírat script a pošle vstupní parametry této funkci.
    - createNewTeam -> vezmu json, projdu všechny názvy týmů a vytvořím je - DONE
    - createNewUser -> vezmu json, projdu všechny emaily uživatelů a vytvořím je - DONE


# Grafana config
/data/infra/grafana/develop/grafana.db
# Návrh řešení
- General složka - default složka může edutovat a zakládat každý a každý bude moc upravovat -> Snaha o vyčištění, zůstanou tu dashboardy, ke kterým se nikdo nepřihlásí
- Konkrétní složka služby - edit pouze konkrétní týmy, které o to budou mít zájem. Vždy musí být alespoň jeden 
- labels - vydefinovat s týmy
- tvoření týmů a přidělování dashboardů manuálně přes GUI - rychlejší než tvoření scriptů -> můžeme se pobavit do budoucna
- zascriptovat vytvoření novýho uživatele -> seznam v jsonu -> test existence uživatele, test existence daného týmu, test existence emailu
- Zachování admin účtu s heslem ve 1pass nad každým prostředím -> putty

# Dotazy:
- jak pracovat se servery - gitlab repo na elk prd, kam můžu ukládat scripty, kam psát readme, kam uložit json, který potřebuju přes curl zavolat 
        - grafana na locale -> grafane.db config
        - git = ops.tools repozitář vlastní branch - https://gitlab.jablotron.cloud/jablotron_ops/ops.tools

- Grafana logy -> bad request, kde k tomu něco dohledám?
    - - v container logs
- docker ps -> můžu sudo

- jak poznám na který env se změny promítnou - pošlu localhost, jakto, že to jede do grafana-dev
    - - docker service ls -> develop = 3000, staging = 3100, production = 3200

- kde je /usr/local/etc/grafana/grafana.ini - potřebuju se dopátrat k auto_assign_org_role, auto_assign_org, mělo by být v .ini souboru, který nemůžu najít 
    - - uvnitř dockeru https://grafana.com/docs/grafana/v9.0/setup-grafana/configure-grafana/#auto-assign-org
    - - v Grafaně je org data - http://grafana-dev.monitoring.local.jablotron.cloud/admin/settings, ale je potřeba měnit v grafana.ini a provést restart

- proč mi neprochází curl -d '{"userId":11}' -X POST http://admin:admin@localhost:3000/api/teams/2/members
    - řešit až na locale

docker service inspect ... manual
sudo docker service inspect monitoring_dev_core_grafana | grep 3000
config - ops.monitoring - core
sudo docker service ls | grep grafana

ENV variables - https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/grafana/#anonymous-authentication
z docker-compose.staging.yml
        -  environment:
      - GF_AUTH_ANONYMOUS_ENABLED=true

## Organization /org/users
- Admin user který má View permission na dashboard může upravovat dashboard všude
- Viewer user nemůže upravovat dashboard nikde, kromě definovaný permission u konkrétního dashboardu
- Rozlišuje se permission u konkrétního dashboardu, ale i podle složky (složka je higher)
- permission prio - org > folder > dashboard

## Per prostředí.json -> develop.json
- default = everyone editor, every folder -> editor = view
- spusť generator -> check for updates.

- Funkce: 
- - Check if user exists -> if exists -> check for updates (nejspíš check for updates jako první a až pak to provolávej)
- - If user doesnt exist -> create if passed details
- - check if e-mail already doesnt exist
- - check if passed team exists
- - check if dashboards exist
- - Dashboardy pro edit = podle týmu + jakýkoliv v "dashboards"

# docker desktop
docker run -d --name=grafana-latest -p 3000:3000 grafana/grafana:9.2.4

# API
https://grafana.com/docs/grafana/latest/developers/http_api/

# Get users
curl http://admin:admin@localhost:3000/api/users

# getDashborad by UID
curl http://admin:admin@localhost:3000/api/dashboards/uid/fv0Zap54k

# Create new user
POST /api/admin/users -d @file.json

# get folder permissions
curl http://admin:admin@localhost:3000/api/folders/poz2Jt54z/permissions

# Default config
- auto_assign_org_role: viewer
- auto_assign_org: 1

# list all running services
systemctl --state=active

# Get Team by name - Not found = "totalCount": 0
curl http://admin:admin@localhost:3000/api/teams/search?query=MyTestTeam | jq .


# Get user id by email
curl http://admin:admin@localhost:3000/api/users?query=jiri.turyna@jablotron.cz

# Get all folders
curl http://admin:admin@localhost:3000/api/folders | jq .
# Get folder by uid 
- test dashboard: http://grafana-dev.monitoring.local.jablotron.cloud/d/3KtLGPv4k/test-dashboard?orgId=1
- test dashboard uid: JR11MPDVz

curl http://admin:admin@localhost:3000/api/folders/JR11MPDVz | jq .

# Get folder permissions
- test dashboard uid: JR11MPDVz

curl http://admin:admin@localhost:3000/api/folders/JR11MPDVz/permissions | jq .

- Je vidět ID týmu a jaký má permission pro dannou složku 

# Add team
- nefunguje, rozchodil jsem v pythonu
curl -X POST -d @newTeam.json http://admin:admin@localhost:3000/api/teams -H "Accept: application/json" 

# Add user to team
- potřeba userId a teamId
- teamId: 3 (MyTestTeam)
- userId: 2 (jiri.turyna@jablotron.cz)


curl -d '{"userId":2}' -X POST http://admin:admin@localhost:3000/api/teams/3/members

# get Dashboards 
curl http://admin:admin@localhost:3000/api/search -H "Accept: application/json" | jq .

# Step by Step
- 1) Spojit se s týmem
- 2) Oflagovat existující dashboardy (i v General složce), které tým vnímá, že patří jim
- 3) Vytvořit složku týmu
- 4) Přesunout dashboardy z bodu 2) do složky týmu
- 5) Přidat nový tým / check existence
- 6) Přidat týmu edit na jejich složku
- 7) Doplnit uživatele do týmu
- 8) Zrevidovat, že každý uživatel kromě Admina má "jen" viewera
- 9) Nastavit všechny foldery na role Editor = View
- 10) Check, že každý dashboard je ve složce
- 11) Check, že neexistuje složka, kterou nemůže nikdo editovat

# Parametry
- 1) nothing
- 2) Generates: Názvy dashboardů, název týmů, seznam uživatelů
- 3) Needs: Název týmu (2)
- 4) Needs: Názvy dashboardů (2)
- 5) Needs: Název týmu (3)
- 6) Needs: Název týmu (2 - dashboardy už jsou ve složce, složka je podle názvu týmu)
- 7) Seznam uživatelů + název týmu
- 8) Seznam všech uživatelů (vytáhni si seznam z API)
- 9) Seznam všech složek (vytáhni si seznam z API)
- 10) Seznam všech dashboardů (vytáhni si seznam z API)
- 11) Seznam všech složek (vytáhni si seznam z API)

# Funkce 
- 3) Check existence, Založ složku -> Vrací True = povedlo se, False = tým už existuje
- 4) Přesuň dashboardy do složky
- 5) Check existence, vytvoř tým
- 6) Přidání permissions týmu pro edit složky
- 7) Check existence, Vytvoř usera, přidej uživatele do týmu
- 8) Check permissions pro každého existujícího uživatele
- 9) Set všech existujících folder permissions pro  roli Editor = View
- 10) Check všech existujících dashboardů, že je může editovat i někdo jiný než admin

# Test all scripts
- ls */*.py|xargs -n 1 -P 3 python3

# Get all users within the current organization
- only works with Basic Authentication
curl http://admin:admin@localhost:3000/api/orgs/1/users | jq .

# Check všech existujících dashboardů, že je může editovat i někdo jiný než admin
- Seznam všech dashboardů -> podle existence -> nemá FolderTitle
- permissions pro každý takový dashboard
- check, že má někde permission: "2"

# Dashboard Inherited Permissions from Folder
- vrací list permissions pro Folder
