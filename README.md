# Grafana

Nastavení DEV - import na STG - import na PRD
# ELK PRD 1
192.168.24.204

# Návrh řešení
- General složka - default složka může edutovat a zakládat každý a každý bude moc upravovat -> Snaha o vyčištění, zůstanou tu dashboardy, ke kterým se nikdo nepřihlásí
- Konkrétní složka služby - edit pouze konkrétní týmy, které o to budou mít zájem. Vždy musí být alespoň jeden 
- labels - vydefinovat s týmy
- tvoření týmů a přidělování dashboardů manuálně přes GUI - rychlejší než tvoření scriptů -> můžeme se pobavit do budoucna
- zascriptovat vytvoření novýho uživatele -> seznam v jsonu -> test existence uživatele, test existence daného týmu, test existence emailu
- Zachování admin účtu s heslem ve 1pass nad každým prostředím -> putty

# Todo
- hidnout foldery/Dashboardy na úrovni organizace - např. externí firmě
    - například remove viewer pro folder

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

# docker desktop
docker run -d -v C:\Docker\grafana:/var/lib/grafana --name=grafana-latest -p 3000:3000 grafana/grafana:9.2.4

# Get users
curl http://admin:admin@localhost:3000/api/users

# Create new user
POST /api/admin/users -d @file.json

# Default config
- auto_assign_org_role: viewer
- auto_assign_org: 1

# Add user to team
- potřeba userId a teamId
- teamId: 2 (Putty)
- userId: 11 (jiri.turyna@jablotron.cz)


curl -d '{"userId":11}' -X POST http://admin:admin@localhost:3000/api/teams/2/members

# Get team id by name
curl http://admin:admin@localhost:3000/api/teams/search?query=Putty

# Get user id by email
curl http://admin:admin@localhost:3000/api/users?query=jiri.turyna@jablotron.cz

# list all running services
systemctl --state=active