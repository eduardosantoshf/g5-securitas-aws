# Deployment

We used [Docker](https://www.docker.com/) to deploy the Human Detection Module (HDM), the docker-compose file is as follows:

~~~yaml
version: "3.8"
services:
    rabbitmq3:
        container_name: "rabbitmq"
        image: rabbitmq:3.8-management-alpine
        environment:
            - RABBITMQ_DEFAULT_USER=myuser
            - RABBITMQ_DEFAULT_PASS=mypassword
        ports:
            # AMQP protocol port
            - '5672:5672'
            # HTTP management UI
            - '15672:15672'

    redis:
        container_name: "redis_db"
        image: redis:6.2-alpine
        restart: always
        ports:
        - '6379:6379'
        command: redis-server --save 20 1 --loglevel warning
        volumes: 
        - redis:/data
    
    camera:
        build:
            context: camera
            dockerfile: Dockerfile
        restart: on-failure

        # environment variable
        environment:
            AMQP_URL: "rabbitmq3"

        depends_on:
            - rabbitmq3
  
    human-detection-module:
        build:
            context: human-detection-module
            dockerfile: Dockerfile
        restart: on-failure

        # environment variable
        environment:
            AMQP_URL: "rabbitmq3"

        depends_on:
            - rabbitmq3
            - redis

volumes:
    redis:
        driver: local
~~~

We can see that we have both the [RabbitMQ](https://www.rabbitmq.com/) and the [Redis](https://redis.io/) services, as well as both the cameras and the human detection modules. Each modules image is described by a Dockerfile.

Cameras Dockerfile:

~~~dockerfile
FROM python:3.9
COPY . /code/
WORKDIR /code/
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
CMD ["python3", "main.py"]
~~~

Human Detection Modules Dockerfile:

~~~dockerfile
FROM python:3.9
COPY . /code/
WORKDIR /code/
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
CMD ["python3","-u", "main.py"]
~~~

Both Dockerfiles installs the need requirements for each module, then runs the modules script.

In the HDM, and regarding the Advanced Message Queuing Protocol (AMQP), the cameras act as producers, and the human detection module (and its instances) act as consumers.