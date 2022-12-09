from fastapi_keycloak import FastAPIKeycloak
import os

# server_url = os.environ.get('IDP_SERVER_URL')
# client_id = os.environ.get('IDP_CLIENT_ID')
# client_secret = os.environ.get('IDP_CLIENT_SECRET')
# admin_client_secret = os.environ.get('IDP_ADMIN_CLIENT_SECRET')
# realm = os.environ.get('IDP_REALM')
# callback_uri = os.environ.get('IDP_CALLBACK_URI')

server_url = "http://keycloak:8080"
client_id = "sites-man-api"
client_secret = "lWacDWzN1T9blKLFpK2Zuz1zZe9uDYaf"
admin_client_secret = "FiX4KgaZ1LCs7IHXaff5sbnxHOdInpvF"
realm = "g5-securitas"
callback_uri = "http://sitesmanagementapi-api-1:8070/callback"
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