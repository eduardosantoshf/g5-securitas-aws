import Keycloak from "keycloak-js";
const keycloak = new Keycloak({
 url: "https://0.0.0.0:8443",
 realm: "g5-securitas",
 clientId: "g5-securitas",
});

export default keycloak; 