import Keycloak from "keycloak-js";
const keycloak = new Keycloak({
 url: "http://192.168.1.76:8080",
 realm: "g5-securitas",
 clientId: "client-ui",
});

export default keycloak; 