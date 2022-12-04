from fastapi_keycloak import FastAPIKeycloak
import os

# server_url = os.environ.get('IDP_SERVER_URL')
# client_id = os.environ.get('IDP_CLIENT_ID')
# client_secret = os.environ.get('IDP_CLIENT_SECRET')
# admin_client_secret = os.environ.get('IDP_ADMIN_CLIENT_SECRET')
# realm = os.environ.get('IDP_REALM')
# callback_uri = os.environ.get('IDP_CALLBACK_URI')

server_url = "http://securitas-lb-1725284772.eu-west-3.elb.amazonaws.com:8080"
client_id = "sites-man-api"
client_secret = "NUdqjNmpQ3VC5WlAfeD5i1thXDUoX8gq"
admin_client_secret = "YqdE6aVoZXCSdLnFtOSgWMQp6viBgM0d"
realm = "g5-securitas"
callback_uri = "http://securitas-lb-1725284772.eu-west-3.elb.amazonaws.com:8080"

idp = None
idp = FastAPIKeycloak(
    server_url=server_url,
    client_id=client_id,
    client_secret=client_secret,
    admin_client_secret=admin_client_secret,
    realm=realm,
    callback_uri=callback_uri
)