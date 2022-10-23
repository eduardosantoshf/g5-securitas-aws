---
sidebar_position: 3
---

# Deployment

The Management UI is deployed with the [AWS Amplify](https://aws.amazon.com/amplify/) service.

There is a pipeline to deploy the Management UI in the AWS Amplify service. The pipeline is triggered when a new commit is pushed to the `development` branch.

~~~yml 
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - cd management-ui
        - yarn install
    build:
      commands:
      - yarn build
  artifacts:
    baseDirectory: ./management-ui/build
    files:
      - '**/*'
  cache:
    paths: 
    - node_modules/**/*
~~~

In order to the build be successful, it is necessary to add the following code on **Custom headers** in the **App settings** of the AWS Amplify service:

~~~yml
customHeaders:
  - pattern: '**'
    headers:
      - key: Cross-Origin-Opener-Policy
        value: same-origin
      - key: Cross-Origin-Embedder-Policy
        value: require-corp
      - key: Access-Control-Allow-Origin
        value: '*'
      - key: Access-Control-Allow-Methods
        value: GET
~~~

After this, we can run the the deploy, and the React app will be deployend in the AWS Amplify service.

For more information about the AWS Amplify service, please check the [AWS Amplify - Getting Started](https://aws.amazon.com/getting-started/hands-on/build-react-app-amplify-graphql/module-one/).
