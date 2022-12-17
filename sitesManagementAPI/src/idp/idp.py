from fastapi_keycloak import FastAPIKeycloak
import os

idp = FastAPIKeycloak(
    server_url=os.environ.get('IDP_SERVER_URL'),
    client_id=os.environ.get('IDP_CLIENT_ID'),
    client_secret=os.environ.get('IDP_CLIENT_SECRET'),
    admin_client_secret=os.environ.get('IDP_ADMIN_CLIENT_SECRET'),
    realm=os.environ.get('IDP_REALM'),
    callback_uri=os.environ.get('IDP_CALLBACK_URI')
)