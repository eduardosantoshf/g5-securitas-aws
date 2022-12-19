---
sidebar_position: 3
---

# Deployment

We deployed our Keycloak server in an EC2 instance in AWS.
First of all we need to install docker and nginx in our EC2 instance.


The IDP module is composed of 2 docker containers. A mariaDB container and a keycloak container.


The deployment pipeline of this system module, uses Github Actions, to run the workflow either when a commit is pushed, or a Pull Request is made to the main branch; this workflow can also be manually run. The full workflow can be found [here](https://github.com/eduardosantoshf/es-project/blob/development/.github/workflows/sites-management-api-deploy.yml).


After the deplyoment workflow has finished, the IDP service can then be accessed through the following link:

[http://securitas-lb-1725284772.eu-west-3.elb.amazonaws.com:8080/](http://securitas-lb-1725284772.eu-west-3.elb.amazonaws.com:8080/)

and the Admin console through the [/admin](http://securitas-lb-1725284772.eu-west-3.elb.amazonaws.com:8080/admin) path.

In a real scenario both these interfaces shouldn't be made available publicly. 


## Realm Configurations 

As the AWS service to permit our data to be persistent is a paid service, we decided to keep a `json` file with all the realm configurations for our system, which we then manually import through the Keycloak admin console web interface. 


## Client Configurations

Our clients also require additional set up before being fully usable. As our configurations are directly imported, it is not possible to reuse the previously generated secrets, so it is required to first deploy the IDP service, generate the client secrets and then deploy the client services with those secrets set up.