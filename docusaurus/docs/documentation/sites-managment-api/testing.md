---
sidebar_position: 4
---

# Testing

To test the application you must first build and deploy the container, check [Deployment](./deployment.md).

Once you have finished launching the application you can then access the API container by executing the following command:

`docker exec -it sitesmanagementapi-api-1 bash`

Finally, in the bash, execute:

`root@api:/usr/app# pytest`

If everything went well you will see a window with information on test results.

**Example:**

![testExample](./tests.png)

