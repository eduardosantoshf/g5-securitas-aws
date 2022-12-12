from fastapi_keycloak import FastAPIKeycloak
import os

# server_url = os.environ.get('IDP_SERVER_URL')
# client_id = os.environ.get('IDP_CLIENT_ID')
# client_secret = os.environ.get('IDP_CLIENT_SECRET')
# admin_client_secret = os.environ.get('IDP_ADMIN_CLIENT_SECRET')
# realm = os.environ.get('IDP_REALM')
# callback_uri = os.environ.get('IDP_CALLBACK_URI')

server_url = "http://172.24.0.4:8080"
client_id = "sites-man-api"
client_secret = "yokvqXNGK5aipoYsbuR50dbHW2dW8t2m"
admin_client_secret = "I5HOlChZu372L7e77WAkgRcdowfeAnsr"
realm = "g5-securitas"
callback_uri = "http://172.24.0.2:8070/callback"
timeout = 50

idp = None
idp = FastAPIKeycloak(
    server_url=server_url,
    client_id=client_id,
    client_secret=client_secret,
    admin_client_secret=admin_client_secret,
    realm=realm,
    callback_uri=callback_uri
)