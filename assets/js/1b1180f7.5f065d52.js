"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[9057],{3905:(e,t,a)=>{a.d(t,{Zo:()=>l,kt:()=>h});var i=a(7294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function n(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,i)}return a}function s(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?n(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):n(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,i,r=function(e,t){if(null==e)return{};var a,i,r={},n=Object.keys(e);for(i=0;i<n.length;i++)a=n[i],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(i=0;i<n.length;i++)a=n[i],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var c=i.createContext({}),u=function(e){var t=i.useContext(c),a=t;return e&&(a="function"==typeof e?e(t):s(s({},t),e)),a},l=function(e){var t=u(e.components);return i.createElement(c.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return i.createElement(i.Fragment,{},t)}},d=i.forwardRef((function(e,t){var a=e.components,r=e.mdxType,n=e.originalType,c=e.parentName,l=o(e,["components","mdxType","originalType","parentName"]),d=u(a),h=r,g=d["".concat(c,".").concat(h)]||d[h]||p[h]||n;return a?i.createElement(g,s(s({ref:t},l),{},{components:a})):i.createElement(g,s({ref:t},l))}));function h(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var n=a.length,s=new Array(n);s[0]=d;var o={};for(var c in t)hasOwnProperty.call(t,c)&&(o[c]=t[c]);o.originalType=e,o.mdxType="string"==typeof e?e:r,s[1]=o;for(var u=2;u<n;u++)s[u]=a[u];return i.createElement.apply(null,s)}return i.createElement.apply(null,a)}d.displayName="MDXCreateElement"},1961:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>c,contentTitle:()=>s,default:()=>p,frontMatter:()=>n,metadata:()=>o,toc:()=>u});var i=a(7462),r=(a(7294),a(3905));const n={sidebar_position:4},s="AWS cloud architecture",o={unversionedId:"aws-cloud-architecture/aws-cloud-architecture",id:"aws-cloud-architecture/aws-cloud-architecture",title:"AWS cloud architecture",description:"architecture image",source:"@site/docs/aws-cloud-architecture/aws-cloud-architecture.md",sourceDirName:"aws-cloud-architecture",slug:"/aws-cloud-architecture/",permalink:"/es-project/aws-cloud-architecture/",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/aws-cloud-architecture/aws-cloud-architecture.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Techologies Used",permalink:"/es-project/techologies-used/"},next:{title:"Documentation",permalink:"/es-project/category/documentation"}},c={},u=[{value:"VPC structure",id:"vpc-structure",level:2},{value:"Routing",id:"routing",level:3},{value:"API Gateway + Elastic load balancer",id:"api-gateway--elastic-load-balancer",level:2},{value:"Security groups",id:"security-groups",level:2},{value:"Human detection service (human-detection-security-group)",id:"human-detection-service-human-detection-security-group",level:3},{value:"Intrusion management API (intrusion-management-api-security-group)",id:"intrusion-management-api-intrusion-management-api-security-group",level:3},{value:"Load balancer (lb-security-group)",id:"load-balancer-lb-security-group",level:3},{value:"Sites management API (sites-man-security-group)",id:"sites-management-api-sites-man-security-group",level:3},{value:"Web UI client (web-ui-client-security-group)",id:"web-ui-client-web-ui-client-security-group",level:3},{value:"Web UI management (web-ui-management-security-group)",id:"web-ui-management-web-ui-management-security-group",level:3},{value:"IDP (idp-security-group)",id:"idp-idp-security-group",level:3},{value:"Service deployment",id:"service-deployment",level:2}],l={toc:u};function p(e){let{components:t,...n}=e;return(0,r.kt)("wrapper",(0,i.Z)({},l,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"aws-cloud-architecture"},"AWS cloud architecture"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"architecture image",src:a(8453).Z,width:"1081",height:"1851"})),(0,r.kt)("h2",{id:"vpc-structure"},"VPC structure"),(0,r.kt)("p",null,"Our VPC is available in 2 availability zones (eu-west-3a and eu-west-3b), providing high availability for our services. Each service has 2 dedicated subnets, one for each availability zone.\nThere are one additional pair of subnets (default-subnet-public) that is used for general AWS services (e.g elastic load balancer (ELB))."),(0,r.kt)("p",null,'Even though we have 2 "private" subnets they are not truly private since they are given a dynamic public IP and that they route outside traffic to the internet gateway, i.e. private subnets share the routing table with public subnets. We were forced to make this decision since the AWS free tier doesn\'t provide NAT gateways for free.'),(0,r.kt)("blockquote",null,(0,r.kt)("p",{parentName:"blockquote"},(0,r.kt)("strong",{parentName:"p"},"NOTE:"),"\nIn the case of the intrusion management API and sites management API because they rely on a local database container we are limited to a single EC2 instance, even though does services are deployed in a scalable cluster. This can be solved be using a service like RDS (relational database service) that provides higher availability. We intend to migrate to this alternative in the future.")),(0,r.kt)("h3",{id:"routing"},"Routing"),(0,r.kt)("p",null,"Since each EC2 is given a random public IP address and that elastic IP address service is not available in the free tier, the routing is handled by the ELB together with the API Gateway. When a service or a client issues a request to the API Gateway it's forwarded to the ELB that is responsible to route it to the appropriate place."),(0,r.kt)("h2",{id:"api-gateway--elastic-load-balancer"},"API Gateway + Elastic load balancer"),(0,r.kt)("p",null,"The API Gateway is responsible to map all the service and user's requests to the corresponding service request. The resulting request is then forwarded to the ELB and delivered to the right EC2 instance group."),(0,r.kt)("p",null,"The ELB listens for HTTP requests delivered by the gateway and then chooses the appropriate service (target group) based on the URL.\n",(0,r.kt)("img",{alt:"listener rules",src:a(2549).Z,width:"1561",height:"402"})),(0,r.kt)("p",null,"To determine which EC2 instance is active at a given time, and therefore capable to handle the request, a period health check is performed. Requests are then only forwarded to active instances.\n",(0,r.kt)("img",{alt:"health check",src:a(3252).Z,width:"1599",height:"398"})),(0,r.kt)("h2",{id:"security-groups"},"Security groups"),(0,r.kt)("p",null,"Each service has its security group allowing inbound traffic according to the service protocols and ports that it uses. For simplicity, all outbound traffic is allowed. In the future, a more elaborate set of rules outbound must be applied."),(0,r.kt)("blockquote",null,(0,r.kt)("p",{parentName:"blockquote"},(0,r.kt)("strong",{parentName:"p"},"NOTE:"),"\nFor the inbound ssh traffic, we allow every ipv4 address to open ssh session from the outside. This is possible since all networks are connected to the internet gateway as explained in ",(0,r.kt)("a",{parentName:"p",href:"#VPC-structure"},"VPC structure"),". Despite simple, is not the optimal solution. In a real scenario the private subnets would not be accessible from the outside nor would we want to allow ssh traffic from the internet. The correct solution would be to place a static bastion server in a public subnet that allows ssh from specific machines, all other instances would allow ssh only from the bastion.")),(0,r.kt)("h3",{id:"human-detection-service-human-detection-security-group"},"Human detection service (human-detection-security-group)"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"security group image",src:a(1740).Z,width:"1588",height:"254"})),(0,r.kt)("h3",{id:"intrusion-management-api-intrusion-management-api-security-group"},"Intrusion management API (intrusion-management-api-security-group)"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"security group image",src:a(6401).Z,width:"1600",height:"251"})),(0,r.kt)("h3",{id:"load-balancer-lb-security-group"},"Load balancer (lb-security-group)"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"security group image",src:a(3204).Z,width:"1599",height:"178"})),(0,r.kt)("h3",{id:"sites-management-api-sites-man-security-group"},"Sites management API (sites-man-security-group)"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"security group image",src:a(4002).Z,width:"1601",height:"226"})),(0,r.kt)("h3",{id:"web-ui-client-web-ui-client-security-group"},"Web UI client (web-ui-client-security-group)"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"security group image",src:a(5479).Z,width:"1600",height:"222"})),(0,r.kt)("h3",{id:"web-ui-management-web-ui-management-security-group"},"Web UI management (web-ui-management-security-group)"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"security group image",src:a(4444).Z,width:"1605",height:"222"})),(0,r.kt)("h3",{id:"idp-idp-security-group"},"IDP (idp-security-group)"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"security group image",src:a(2611).Z,width:"1597",height:"204"})),(0,r.kt)("h2",{id:"service-deployment"},"Service deployment"),(0,r.kt)("p",null,"Every service is deployed using the elastic container service (ECS). This allows us to scale our services up and down at any time and to easily shut them down when they are not in use. The deployment workflow is automated using github actions."),(0,r.kt)("p",null,"After passing the code validation tests the updated services can be deployed by committing to the main branch or by triggering the corresponding workflows manually. "),(0,r.kt)("p",null,"The deployment process performs the following steps:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Log in to the AWS account using the secrets in us-east-1 region."),(0,r.kt)("li",{parentName:"ul"},"Build the container and push it public elastic container registry (ECR)."),(0,r.kt)("li",{parentName:"ul"},"Change region to eu-west-3."),(0,r.kt)("li",{parentName:"ul"},"Update cluster service task to point to the newly created container image and insert relevant environment variables."),(0,r.kt)("li",{parentName:"ul"},"Finally, upload the previously updated task to AWS.")),(0,r.kt)("p",null,"At the of the process, the corresponding service is updated."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"NOTE:"),"\nWe are using the public ECR do to the 500MB limitation for the private registry. We have to first login into us-east-1 to access the public registry and then change to eu-west-3, our VPC region."))}p.isMDXComponent=!0},8453:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/AWS_cloud_architecture-800ca1ffba426af2bb14347fc94d1b43.jpg"},3252:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/ELB_Health_check-0a0472140b50e6abc3279803ec178a82.jpg"},2549:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/ELB_Listener_rules-fb437df2b728f20a704d75cc6ebb11cc.jpg"},1740:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/human-detection-security-group-e1c8a9d2151f9f32944e71b64f433d22.jpg"},2611:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/idp-security-group-f545e9044d20974f22b864aaea4fa03f.jpg"},6401:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/intrusion-management-api-security-group-e616eac5aa0001eebdc96791366ed38b.jpg"},3204:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/lb-security-group-25c5ec1765a8203c830b9eef0d45a746.jpg"},4002:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/sites-man-security-group-86654459925bf52852a588b2672320b5.jpg"},5479:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/web-ui-client-security-group-71c982fb8f0222143db26e312713d432.jpg"},4444:(e,t,a)=>{a.d(t,{Z:()=>i});const i=a.p+"assets/images/web-ui-management-security-group-1860cb9b0f5431c622a132d628221b59.jpg"}}]);