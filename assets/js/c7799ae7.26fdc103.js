"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[8227],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>d});var r=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function s(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function i(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},a=Object.keys(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var c=r.createContext({}),l=function(e){var t=r.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):s(s({},t),e)),n},p=function(e){var t=l(e.components);return r.createElement(c.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var n=e.components,o=e.mdxType,a=e.originalType,c=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),m=l(n),d=o,g=m["".concat(c,".").concat(d)]||m[d]||u[d]||a;return n?r.createElement(g,s(s({ref:t},p),{},{components:n})):r.createElement(g,s({ref:t},p))}));function d(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=n.length,s=new Array(a);s[0]=m;var i={};for(var c in t)hasOwnProperty.call(t,c)&&(i[c]=t[c]);i.originalType=e,i.mdxType="string"==typeof e?e:o,s[1]=i;for(var l=2;l<a;l++)s[l]=n[l];return r.createElement.apply(null,s)}return r.createElement.apply(null,n)}m.displayName="MDXCreateElement"},5510:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>s,default:()=>u,frontMatter:()=>a,metadata:()=>i,toc:()=>l});var r=n(7462),o=(n(7294),n(3905));const a={sidebar_position:1},s="Deployment",i={unversionedId:"documentation/sites-managment-api/deployment",id:"documentation/sites-managment-api/deployment",title:"Deployment",description:"We deployed our API in an EC2 instance in AWS.",source:"@site/docs/documentation/sites-managment-api/deployment.md",sourceDirName:"documentation/sites-managment-api",slug:"/documentation/sites-managment-api/deployment",permalink:"/es-project/documentation/sites-managment-api/deployment",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/documentation/sites-managment-api/deployment.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Sites Managment API",permalink:"/es-project/category/sites-managment-api"},next:{title:"API Documentation",permalink:"/es-project/documentation/sites-managment-api/api-documentation"}},c={},l=[],p={toc:l};function u(e){let{components:t,...n}=e;return(0,o.kt)("wrapper",(0,r.Z)({},p,n,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"deployment"},"Deployment"),(0,o.kt)("p",null,"We deployed our API in an EC2 instance in AWS.\nFirst of all we need to install docker and nginx in our EC2 instance."),(0,o.kt)("p",null,"The Sites management API module is composed of 2 docker containers. A mariaDB container and a Fast-API container."),(0,o.kt)("p",null,"We use a docker-compose file to run the containers:"),(0,o.kt)("p",null,(0,o.kt)("inlineCode",{parentName:"p"},"docker compose -f docker-compose-dev.yml up --build")),(0,o.kt)("p",null,"After that we need to configure nginx to redirect the requests to the Fast-API container. As we have our front-end (management-ui) using HTTPS so that we need to configure nginx to use HTTPS too, like the following configuration at /etc/nginx/sites-enabled/fastapi_nginx:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"sudo apt-get install openssl\ncd /etc/nginx/\nsudo mkdir ssl\nsudo openssl req -batch -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/server.key -out /etc/nginx/ssl/server.crt\n")),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-nginx"},"server {\n        listen 80;\n        listen 443 ssl;\n        ssl on;\n        ssl_certificate /etc/nginx/ssl/server.crt;\n        ssl_certificate_key /etc/nginx/ssl/server.key;\n        server_name 52.215.207.18;\n        location / {\n                proxy_pass http://0.0.0.0:8000;\n                add_header 'Access-Control-Allow-Origin' '*';\n                add_header 'Access-Control-Allow-Methods' 'GET, POST, DELETE, OPTIONS';\n                add_header 'Content-Security-Policy' 'upgrade-insecure-requests';\n        }\n}\n\n")),(0,o.kt)("p",null,"After that we need to restart nginx service:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"sudo systemctl restart nginx\nsudo systemctl status nginx\n")),(0,o.kt)("p",null,"At this point, you should be able to access the API using the following URL: "),(0,o.kt)("p",null,(0,o.kt)("a",{parentName:"p",href:"https://52.215.207.18/"},"https://52.215.207.18")))}u.isMDXComponent=!0}}]);