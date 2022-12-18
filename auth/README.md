## Usage
On first boot, import the realm configuration

```
docker-compose up --build

docker cp ./realm-export.json auth-keycloak-1:/opt/keycloak/realm-export.json

docker exec -ti auth-keycloak-1 bash

/opt/keycloak/bin/kc.sh import --file realm-export.json
```
Ignore the errors