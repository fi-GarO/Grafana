# Grafana

## Connect ELK-PRD1
- VPN
ssh jturyna@192.168.24.204

## Grafana config
/data/infra/grafana/develop/grafana.db
## API
https://grafana.com/docs/grafana/latest/developers/http_api/
## GET Users
curl http://admin:admin@localhost:3000/api/users | jq .
## Get Team by name - Not found = "totalCount": 0
curl http://admin:admin@localhost:3000/api/teams/search?query=Putty | jq .

## Get all folders
curl http://admin:admin@localhost:3000/api/folders | jq .
## Get folder by uid 
- test dashboard: http://grafana-dev.monitoring.local.jablotron.cloud/d/3KtLGPv4k/test-dashboard?orgId=1
- test dashboard uid: JR11MPDVz

curl http://admin:admin@localhost:3000/api/folders/JR11MPDVz | jq .

## Get folder permissions
- test dashboard uid: JR11MPDVz

curl http://admin:admin@localhost:3000/api/folders/JR11MPDVz/permissions | jq .

- Je vidět ID týmu a jaký má permission pro dannou složku 
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



## Dotazy
- Kam cpát python scripty a dokumentaci
- Jak se pozná, který environment provolávám -> swarm-endpoints.json 3000 je Grafana, ale nevím jaké 
    docker ps -> permission denied
- Grafana z Gitlabu
- auto_assign_org_role??