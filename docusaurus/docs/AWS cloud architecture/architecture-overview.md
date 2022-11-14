---
sidebar_position: 1
---

# High level overview

![architecture image](images/AWS%20Cloud%20Architecture.drawio.png)

## Service deployment

Every service is deployed using the elastic container service (ECS). This allows us to scale our services up and down at any time and to easily shut them down when they are not in use. The deployment workflow is automated using github actions.

## VPC structure

Our VPC is available in 2 availability zones (eu-west-3a and eu-west-3b), providing high availability for our services. Each service has 2 dedicated subnets, one for each availability zone.
There are one additional pair of subnets (default-subnet-public) that is used for general AWS services (e.g elastic load balancer (ELB))

### Routing

Since each EC2 is given a random public IP address and that elastic IP address service is not available in free tier, the routing is handled by the ELB together with the API Gateway. When a service or a client issues a request to the API Gateway it's forwarded to the ELB that is responsible to route it to the appropriate place.

# API Gateway


