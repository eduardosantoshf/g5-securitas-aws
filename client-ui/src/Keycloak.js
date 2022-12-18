import Keycloak from "keycloak-js";
const keycloak = new Keycloak({
//  url: "http://172.18.0.4:8080",
 url: process.env.REACT_APP_KEYCLOAK_URL,
 realm: "g5-securitas",
 clientId: "client-ui",
//  clientSecret: "f9Gm50FbmFQld5NieiDLehRCoHNN3uNf",
//  grantType: "password",
//  credentials: {
//     secret: "f9Gm50FbmFQld5NieiDLehRCoHNN3uNf",
//     }
});

export default keycloak; 