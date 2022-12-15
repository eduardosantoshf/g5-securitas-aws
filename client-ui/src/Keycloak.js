import Keycloak from "keycloak-js";
const keycloak = new Keycloak({
 url: "http://172.27.0.3:8080",
 realm: "g5-securitas",
 clientId: "client-ui",
//  clientSecret: "f9Gm50FbmFQld5NieiDLehRCoHNN3uNf",
//  grantType: "password",
//  credentials: {
//     secret: "f9Gm50FbmFQld5NieiDLehRCoHNN3uNf",
//     }
});

export default keycloak; 