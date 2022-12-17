import Keycloak from "keycloak-js";
const keycloak = new Keycloak({
 url: "http://172.18.0.2:8080",
 realm: "g5-securitas",
 clientId: "management-ui",
});

export default keycloak; 