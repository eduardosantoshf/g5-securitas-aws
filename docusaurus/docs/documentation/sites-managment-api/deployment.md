---
sidebar_position: 1
---

# Deployment

We deployed our API in an EC2 instance in AWS.
First of all we need to install docker and nginx in our EC2 instance.

The Sites management API module is composed of 2 docker containers. A mariaDB container and a Fast-API container.

We use a docker-compose file to run the containers:


`docker compose -f docker-compose-dev.yml up --build`

After that we need to configure nginx to redirect the requests to the Fast-API container. As we have our front-end (management-ui) using HTTPS so that we need to configure nginx to use HTTPS too, like the following configuration at /etc/nginx/sites-enabled/fastapi_nginx:

```bash
sudo apt-get install openssl
cd /etc/nginx/
sudo mkdir ssl
sudo openssl req -batch -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/server.key -out /etc/nginx/ssl/server.crt
```

```nginx
server {
        listen 80;
        listen 443 ssl;
        ssl on;
        ssl_certificate /etc/nginx/ssl/server.crt;
        ssl_certificate_key /etc/nginx/ssl/server.key;
        server_name 52.215.207.18;
        location / {
                proxy_pass http://0.0.0.0:8000;
                add_header 'Access-Control-Allow-Origin' '*';
                add_header 'Access-Control-Allow-Methods' 'GET, POST, DELETE, OPTIONS';
                add_header 'Content-Security-Policy' 'upgrade-insecure-requests';
        }
}

```

After that we need to restart nginx service:

```bash
sudo systemctl restart nginx
sudo systemctl status nginx
```

At this point, you should be able to access the API using the following URL: 

[https://52.215.207.18](https://52.215.207.18/)

