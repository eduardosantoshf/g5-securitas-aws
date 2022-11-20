import Keycloak from "keycloak-js";
const keycloak = new Keycloak({
 url: "https://0.0.0.0:8443",
 realm: "myrealm",
 clientId: "client1",
});

export default keycloak;