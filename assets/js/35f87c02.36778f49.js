"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[8545],{3905:(e,t,n)=>{n.d(t,{Zo:()=>d,kt:()=>h});var r=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var l=r.createContext({}),s=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},d=function(e){var t=s(e.components);return r.createElement(l.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},u=r.forwardRef((function(e,t){var n=e.components,o=e.mdxType,i=e.originalType,l=e.parentName,d=c(e,["components","mdxType","originalType","parentName"]),u=s(n),h=o,m=u["".concat(l,".").concat(h)]||u[h]||p[h]||i;return n?r.createElement(m,a(a({ref:t},d),{},{components:n})):r.createElement(m,a({ref:t},d))}));function h(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=n.length,a=new Array(i);a[0]=u;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c.mdxType="string"==typeof e?e:o,a[1]=c;for(var s=2;s<i;s++)a[s]=n[s];return r.createElement.apply(null,a)}return r.createElement.apply(null,n)}u.displayName="MDXCreateElement"},5112:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>a,default:()=>p,frontMatter:()=>i,metadata:()=>c,toc:()=>s});var r=n(7462),o=(n(7294),n(3905));const i={sidebar_position:1},a="Identity Provider",c={unversionedId:"documentation/identity-provider/identity-provider",id:"documentation/identity-provider/identity-provider",title:"Identity Provider",description:"The Keycloak was the tool chosen to develop the Identity Provider.",source:"@site/docs/documentation/identity-provider/identity-provider.md",sourceDirName:"documentation/identity-provider",slug:"/documentation/identity-provider/",permalink:"/es-project/documentation/identity-provider/",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/documentation/identity-provider/identity-provider.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Identity Provider",permalink:"/es-project/category/identity-provider"},next:{title:"Testing",permalink:"/es-project/documentation/identity-provider/testing"}},l={},s=[{value:"Keycloak Configuration",id:"keycloak-configuration",level:2},{value:"Frontend integration with IDP",id:"frontend-integration-with-idp",level:2},{value:"Sites Managment API integration with IDP",id:"sites-managment-api-integration-with-idp",level:2}],d={toc:s};function p(e){let{components:t,...i}=e;return(0,o.kt)("wrapper",(0,r.Z)({},d,i,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"identity-provider"},"Identity Provider"),(0,o.kt)("p",null,"The ",(0,o.kt)("a",{parentName:"p",href:"https://www.keycloak.org/"},"Keycloak")," was the tool chosen to develop the Identity Provider."),(0,o.kt)("h2",{id:"keycloak-configuration"},"Keycloak Configuration"),(0,o.kt)("p",null,'The first step was to create a realm for our project, "g5-securitas".'),(0,o.kt)("p",null,'Next, we created 2 roles for the realm in question, one for management users and another for client users, respectively "g5-admin" and "g5-end-users". The default role "default-roles-g5-securitas" is also a role that identifies users as clients.'),(0,o.kt)("p",null,'The management users are configured by the keycloak admin server, where credentials and the "g5-admin" role are assigned, in order to be able to authenticate in the Management UI.'),(0,o.kt)("p",null,"Finally, we created 3 clients, one for the Managment Web UI, another for the Client Web UI and for the Sites Managment API."),(0,o.kt)("h2",{id:"frontend-integration-with-idp"},"Frontend integration with IDP"),(0,o.kt)("p",null,"In order to integrate the IDP in the frontends we had to install the following dependencies:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},"npm i keycloak-js\nnpm i @react-keycloak/web\n")),(0,o.kt)("p",null,"We create a Keycloak.js file, where we create a Keycloak instance with the Keycloak server URL, with the realm name and the respective frontend ID."),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-javascript"},'import Keycloak from "keycloak-js";\nconst keycloak = new Keycloak({\n url: process.env.REACT_APP_KEYCLOAK_URL,\n realm: process.env.REACT_APP_REALM,\n clientId: process.env.REACT_APP_CLIENT_UI_ID,\n});\n\nexport default keycloak; \n')),(0,o.kt)("p",null,"In the index.js file, we import the < ReactKeycloakProvider /> with the keycloak.js file as a prop. Wraps the entire app with the identity provider"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-javascript"},"import React from 'react';\nimport ReactDOM from 'react-dom/client';\nimport './index.css';\nimport App from './App';\nimport reportWebVitals from './reportWebVitals';\nimport { ReactKeycloakProvider } from \"@react-keycloak/web\";\nimport keycloak from \"./Keycloak\";\n\nconst root = ReactDOM.createRoot(document.getElementById('root'));\nroot.render(\n   <ReactKeycloakProvider authClient={keycloak}>\n    <App />\n   </ReactKeycloakProvider>\n);\n\nreportWebVitals();\n")),(0,o.kt)("p",null,"In both frontends, in the Sidebar we define that the Home page is a public page and the rest are private pages, that is, the Home page can be accessed without authentication, but the rest can only be accessed with authentication."),(0,o.kt)("p",null,"We implemented code in the frontends that checks if there is an authenticated user, if there is it shows a Logout button and the name of the authenticated user, if not it shows the Login button. When the Login button is clicked, Keycloak's Login method is executed to authenticate the user. When the Logout button is clicked, Keycloak's Logout method is executed to Logout of the user's account."),(0,o.kt)("p",null,(0,o.kt)("img",{src:n(4020).Z,width:"602",height:"538"})),(0,o.kt)("p",null,"In the frontends, in each call to the Sites Management API we add the 'Authorization' header with the authenticated user token."),(0,o.kt)("h2",{id:"sites-managment-api-integration-with-idp"},"Sites Managment API integration with IDP"))}p.isMDXComponent=!0},4020:(e,t,n)=>{n.d(t,{Z:()=>r});const r=n.p+"assets/images/login-2658d77a671e442d9699afadacb66188.png"}}]);