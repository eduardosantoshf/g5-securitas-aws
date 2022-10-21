---
sidebar_position: 1
---

# Deployment

The Sites management API module is composed of 2 docker containers. A mariaDB container and a Fast-API container.

To deploy the API in a development environment do to *sitesManagementAPI* folder and run the command:


`docker compose -f docker-compose-dev.yml up --build`

At this point, you should be able to access the API using the following URL: 

[http://localhost:8000/docs](http://localhost:8000).

A swagger UI API documentation page is shown with all the available endpoints with an explanation of how each resource
can be accessed, which parameters are required, and an example response schema. It's also possible to test each
endpoint by clicking **Try it out**.