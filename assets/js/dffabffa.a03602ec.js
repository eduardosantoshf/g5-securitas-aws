"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[8309],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>d});var r=n(7294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,i=function(e,t){if(null==e)return{};var n,r,i={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var c=r.createContext({}),u=function(e){var t=r.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},p=function(e){var t=u(e.components);return r.createElement(c.Provider,{value:t},e.children)},l={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var n=e.components,i=e.mdxType,o=e.originalType,c=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),m=u(n),d=i,f=m["".concat(c,".").concat(d)]||m[d]||l[d]||o;return n?r.createElement(f,a(a({ref:t},p),{},{components:n})):r.createElement(f,a({ref:t},p))}));function d(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=n.length,a=new Array(o);a[0]=m;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:i,a[1]=s;for(var u=2;u<o;u++)a[u]=n[u];return r.createElement.apply(null,a)}return r.createElement.apply(null,n)}m.displayName="MDXCreateElement"},2053:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>a,default:()=>l,frontMatter:()=>o,metadata:()=>s,toc:()=>u});var r=n(7462),i=(n(7294),n(3905));const o={sidebar_position:1},a="Cliping an intrusion",s={unversionedId:"documentation/cameras/cliping-intrusion",id:"documentation/cameras/cliping-intrusion",title:"Cliping an intrusion",description:"When a intrusion occours, the intrusion-management-api, send a message to the broker, where the cameras are subscribed.",source:"@site/docs/documentation/cameras/cliping-intrusion.md",sourceDirName:"documentation/cameras",slug:"/documentation/cameras/cliping-intrusion",permalink:"/es-project/documentation/cameras/cliping-intrusion",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/documentation/cameras/cliping-intrusion.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Cameras",permalink:"/es-project/category/cameras"},next:{title:"CI/CD",permalink:"/es-project/documentation/ci-cd"}},c={},u=[],p={toc:u};function l(e){let{components:t,...o}=e;return(0,i.kt)("wrapper",(0,r.Z)({},p,o,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"cliping-an-intrusion"},"Cliping an intrusion"),(0,i.kt)("p",null,"When a intrusion occours, the intrusion-management-api, send a message to the broker, where the cameras are subscribed.\nThe timestamp of the intrusion is received and the camera start to make a clip of the intrusion with a duration of 10 seconds before and 10 seconds after the intrusion, so the user can see the context of the intrusion."),(0,i.kt)("p",null,"The clip is saved and then, is send to the intrusion-management-api where will be stored in a S3 bucket, on AWS."),(0,i.kt)("p",null,"The following image shows the cliping process:"),(0,i.kt)("p",null,(0,i.kt)("img",{alt:"Cliping process",src:n(251).Z,width:"571",height:"201"})))}l.isMDXComponent=!0},251:(e,t,n)=>{n.d(t,{Z:()=>r});const r=n.p+"assets/images/clipping-process-15ad63804659306d910076ff48366b26.png"}}]);