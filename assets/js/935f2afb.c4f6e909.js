"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[53],{1109:e=>{e.exports=JSON.parse('{"pluginId":"default","version":"current","label":"Next","banner":null,"badge":false,"noIndex":false,"className":"docs-version-current","isLast":true,"docsSidebars":{"tutorialSidebar":[{"type":"link","label":"Introduction to the Project","href":"/es-project/","docId":"intro"},{"type":"category","label":"Architecture","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Architecture Design","href":"/es-project/architecture/architecture-design","docId":"architecture/architecture-design"},{"type":"link","label":"Architecture Specification","href":"/es-project/architecture/arquitecture-specification","docId":"architecture/arquitecture-specification"}],"href":"/es-project/category/architecture"},{"type":"link","label":"Project Members","href":"/es-project/project-members/","docId":"project-members/project-members"},{"type":"link","label":"Techologies Used","href":"/es-project/techologies-used/","docId":"techologies-used/techologies-used"},{"type":"category","label":"Documentation","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"CI/CD","href":"/es-project/documentation/ci-cd","docId":"documentation/ci-cd"},{"type":"category","label":"Client Web UI","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Front-end","href":"/es-project/documentation/client-web-ui/","docId":"documentation/client-web-ui/client-web-ui"},{"type":"link","label":"Testing","href":"/es-project/documentation/client-web-ui/testing","docId":"documentation/client-web-ui/testing"}],"href":"/es-project/category/client-web-ui"},{"type":"category","label":"Human Detection Module","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Deployment","href":"/es-project/documentation/human-detection-module/deployment","docId":"documentation/human-detection-module/deployment"}],"href":"/es-project/category/human-detection-module"},{"type":"category","label":"Management Web UI","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Front-end","href":"/es-project/documentation/management-web-ui/","docId":"documentation/management-web-ui/management-web-ui"},{"type":"link","label":"Testing","href":"/es-project/documentation/management-web-ui/testing","docId":"documentation/management-web-ui/testing"},{"type":"link","label":"Deployment","href":"/es-project/documentation/management-web-ui/deployment","docId":"documentation/management-web-ui/deployment"}],"href":"/es-project/category/management-web-ui"},{"type":"category","label":"Sites Managment API","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Deployment","href":"/es-project/documentation/sites-managment-api/deployment","docId":"documentation/sites-managment-api/deployment"},{"type":"link","label":"API Documentation","href":"/es-project/documentation/sites-managment-api/api-documentation","docId":"documentation/sites-managment-api/api-documentation"},{"type":"link","label":"Tools used","href":"/es-project/documentation/sites-managment-api/tools-used","docId":"documentation/sites-managment-api/tools-used"},{"type":"link","label":"Testing","href":"/es-project/documentation/sites-managment-api/testing","docId":"documentation/sites-managment-api/testing"}],"href":"/es-project/category/sites-managment-api"},{"type":"category","label":"Intrusion Managment API","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Introduction","href":"/es-project/documentation/intrusion-management-api/introduction","docId":"documentation/intrusion-management-api/introduction"},{"type":"link","label":"API Documentation","href":"/es-project/documentation/intrusion-management-api/api-documentation","docId":"documentation/intrusion-management-api/api-documentation"},{"type":"link","label":"Tests","href":"/es-project/documentation/intrusion-management-api/tests","docId":"documentation/intrusion-management-api/tests"},{"type":"link","label":"Deployment","href":"/es-project/documentation/intrusion-management-api/deployment","docId":"documentation/intrusion-management-api/deployment"}],"href":"/es-project/category/intrusion-managment-api"}],"href":"/es-project/category/documentation"},{"type":"category","label":"Definitions about User Stories","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"User Story Readiness Criteria","href":"/es-project/user-stories/user-story-readiness-criteria/","docId":"user-stories/user-story-readiness-criteria/user-story-readiness-criteria"},{"type":"link","label":"User Story Acceptance Criteria","href":"/es-project/user-stories/user-story-acceptance-criteria/","docId":"user-stories/user-story-acceptance-criteria/user-story-acceptance-criteria"},{"type":"link","label":"User Story priorities","href":"/es-project/user-stories/user-story-priorities/","docId":"user-stories/user-story-priorities/user-story-priorities"},{"type":"link","label":"User Story points","href":"/es-project/user-stories/user-story-points/","docId":"user-stories/user-story-points/user-story-points"}],"href":"/es-project/category/definitions-about-user-stories"}]},"docs":{"architecture/architecture-design":{"id":"architecture/architecture-design","title":"Architecture Design","description":"The following diagram shows the architecture design of the Intrusion Detection System:","sidebar":"tutorialSidebar"},"architecture/arquitecture-specification":{"id":"architecture/arquitecture-specification","title":"Architecture Specification","description":"More detailed information about the architecture of the Intrusion Detection System, can be found in the following table:","sidebar":"tutorialSidebar"},"documentation/ci-cd":{"id":"documentation/ci-cd","title":"CI/CD","description":"Testing","sidebar":"tutorialSidebar"},"documentation/client-web-ui/client-web-ui":{"id":"documentation/client-web-ui/client-web-ui","title":"Front-end","description":"The React was the tool chosen to develop the Client Web UI.","sidebar":"tutorialSidebar"},"documentation/client-web-ui/testing":{"id":"documentation/client-web-ui/testing","title":"Testing","description":"The Client Web UI was tested using the Jest framework to run the tests.","sidebar":"tutorialSidebar"},"documentation/human-detection-module/deployment":{"id":"documentation/human-detection-module/deployment","title":"Deployment","description":"We used Docker to deploy the Human Detection Module (HDM), the docker-compose file is as follows:","sidebar":"tutorialSidebar"},"documentation/intrusion-management-api/api-documentation":{"id":"documentation/intrusion-management-api/api-documentation","title":"API Documentation","description":"We use Swagger as our documentation tool, which has out-of-the-box integration with FastAPI and","sidebar":"tutorialSidebar"},"documentation/intrusion-management-api/deployment":{"id":"documentation/intrusion-management-api/deployment","title":"Deployment","description":"","sidebar":"tutorialSidebar"},"documentation/intrusion-management-api/introduction":{"id":"documentation/intrusion-management-api/introduction","title":"Introduction","description":"This API will be used to act whenever an intrusion is detected. It will get the intrusion video clips from the cameras, activate the alarms, and trigger a new notification in the Notifications API.","sidebar":"tutorialSidebar"},"documentation/intrusion-management-api/tests":{"id":"documentation/intrusion-management-api/tests","title":"Tests","description":"The tests are located in the tests folder. You dont neet to have the application running to run the tests, only have to be inside the virtual environment.To run the tests, execute the following command:","sidebar":"tutorialSidebar"},"documentation/management-web-ui/deployment":{"id":"documentation/management-web-ui/deployment","title":"Deployment","description":"The Management UI is deployed with the AWS Amplify service.","sidebar":"tutorialSidebar"},"documentation/management-web-ui/management-web-ui":{"id":"documentation/management-web-ui/management-web-ui","title":"Front-end","description":"The React was the tool chosen to develop the Management Web UI.","sidebar":"tutorialSidebar"},"documentation/management-web-ui/testing":{"id":"documentation/management-web-ui/testing","title":"Testing","description":"The Management Web UI was tested using the Jest framework to run the tests.","sidebar":"tutorialSidebar"},"documentation/sites-managment-api/api-documentation":{"id":"documentation/sites-managment-api/api-documentation","title":"API Documentation","description":"We use Swagger as our documentation tool, which has out-of-the-box integration with FastAPI and","sidebar":"tutorialSidebar"},"documentation/sites-managment-api/deployment":{"id":"documentation/sites-managment-api/deployment","title":"Deployment","description":"We deployed our API in an EC2 instance in AWS.","sidebar":"tutorialSidebar"},"documentation/sites-managment-api/testing":{"id":"documentation/sites-managment-api/testing","title":"Testing","description":"To test the application you must first build and deploy the container, check Deployment.","sidebar":"tutorialSidebar"},"documentation/sites-managment-api/tools-used":{"id":"documentation/sites-managment-api/tools-used","title":"Tools used","description":"- To containerize our service we are using docker.","sidebar":"tutorialSidebar"},"intro":{"id":"intro","title":"Introduction to the Project","description":"This project will tackle the development of a software solution for a security company named SecCom. SecCom is a company that ensures critical buildings are not broken into, through the installation and operation of CCTV cameras on-premises.","sidebar":"tutorialSidebar"},"project-members/project-members":{"id":"project-members/project-members","title":"Project Members","description":"Team 5 of the Software Engineer course:","sidebar":"tutorialSidebar"},"techologies-used/techologies-used":{"id":"techologies-used/techologies-used","title":"Techologies Used","description":"We decide to use the following technologies to build our system:","sidebar":"tutorialSidebar"},"user-stories/user-story-acceptance-criteria/user-story-acceptance-criteria":{"id":"user-stories/user-story-acceptance-criteria/user-story-acceptance-criteria","title":"User Story Acceptance Criteria","description":"Definition of Done","sidebar":"tutorialSidebar"},"user-stories/user-story-points/user-story-points":{"id":"user-stories/user-story-points/user-story-points","title":"User Story points","description":"The process of assigning points to a user story follows these steps:","sidebar":"tutorialSidebar"},"user-stories/user-story-priorities/user-story-priorities":{"id":"user-stories/user-story-priorities/user-story-priorities","title":"User Story priorities","description":"The priority of user stories is given by their order in the product backlog. The higher they are at the top, the higher their priority.","sidebar":"tutorialSidebar"},"user-stories/user-story-readiness-criteria/user-story-readiness-criteria":{"id":"user-stories/user-story-readiness-criteria/user-story-readiness-criteria","title":"User Story Readiness Criteria","description":"Definition of Ready","sidebar":"tutorialSidebar"}}}')}}]);