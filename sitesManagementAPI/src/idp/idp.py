from fastapi_keycloak import FastAPIKeycloak
import os

# server_url = os.environ.get('IDP_SERVER_URL')
# client_id = os.environ.get('IDP_CLIENT_ID')
# client_secret = os.environ.get('IDP_CLIENT_SECRET')
# admin_client_secret = os.environ.get('IDP_ADMIN_CLIENT_SECRET')
# realm = os.environ.get('IDP_REALM')
# callback_uri = os.environ.get('IDP_CALLBACK_URI')

server_url = "http://0.0.0.0:8445/"
client_id = "g5-securitas"
client_secret = "HEZARJwUN6zgQHjducAWO5cvsMCjbcbZ"
admin_client_secret = "fQzhB9dEuZRnqk1GhsnO5AutbvjholmL"
realm = "g5-securitas"
callback_uri = "http://0.0.0.0:3000/"


idp = FastAPIKeycloak(
    server_url=server_url,
    client_id=client_id,
    client_secret=client_secret,
    admin_client_secret=admin_client_secret,
    realm=realm,
    callback_uri=callback_uri
)