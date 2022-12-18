# base code by rafael-direito in ATNoG/VPilot/ResourceManager gh repository
import pytest
from fastapi_keycloak.model import OIDCUser, KeycloakUser
from fastapi_keycloak import KeycloakError
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status


mocked_user_db = []

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class MockOIDCUser(metaclass=Singleton):
    mocked_oidc_user = OIDCUser(
        sub="",
        iat=0,
        exp=0,
        email_verified=True,
        preferred_username="",
        realm_access={
            "roles": []
        },
    )

    def get_mocked_oidc_user(self):
        return self.mocked_oidc_user

    def inject_mocked_oidc_user(self, id, username, roles):
        self.mocked_oidc_user = OIDCUser(
            sub=id,
            iat=0,
            exp=0,
            email_verified=True,
            preferred_username=username,
            realm_access={
                "roles": roles
            },
        )
        
        if not self.mocked_oidc_user.sub in [i.id for i in mocked_user_db]:
            mocked_user_db.append(
                KeycloakUser(
                    id=self.mocked_oidc_user.sub,
                    createdTimestamp=0,
                    username=self.mocked_oidc_user.preferred_username,
                    enabled=True,
                    totp=True,
                    emailVerified=self.mocked_oidc_user.email_verified,
                    disableableCredentialTypes=[],
                    requiredActions=[],
                    notBefore=0,
                    access=self.mocked_oidc_user.realm_access,
                )
            )


class MockFastAPIKeycloak(metaclass=Singleton):

    def user_auth_scheme(self):
        return OAuth2PasswordBearer(tokenUrl="token_uri")

    def get_current_user(required_roles=None):
        def current_user():
            mocked_oidc_user = MockOIDCUser().get_mocked_oidc_user()
            if required_roles:
                for role in required_roles:
                    if role not in mocked_oidc_user.roles:
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Role "{role}" is required to ' +
                            'perform this action',
                        )
            return mocked_oidc_user

        return current_user

    # query search not implemented, returns None type, raise exception if user not found
    def get_user(user_id=None, query=""):
        if user_id is None:
            return None
        else:
            for i in mocked_user_db:
                if user_id == i.id:
                    return i
        raise KeycloakError(
            status_code=status.HTTP_404_NOT_FOUND,
            reason=f'User with id {user_id} not found'
        )
    
    def get_all_users():
        return mocked_user_db

def setup_test_idp(monkeypatch, mocker):
    # mock IDP needed environment variables
    monkeypatch.setenv("IDP_SERVER_URL", "test_defined_env")
    monkeypatch.setenv("IDP_CLIENT_ID", "test_defined_env")
    monkeypatch.setenv("IDP_CLIENT_SECRET", "test_defined_env")
    monkeypatch.setenv("IDP_ADMIN_CLIENT_SECRET", "test_defined_env")
    monkeypatch.setenv("IDP_REALM", "test_defined_env")
    monkeypatch.setenv("IDP_CALLBACK_URI", "test_defined_env")
    # mock IDP initialization
    FastAPIKeycloak_mock = mocker.patch("fastapi_keycloak.FastAPIKeycloak")
    FastAPIKeycloak_mock.return_value = MockFastAPIKeycloak


def inject_admin_user():
    # Prepare Mocked OIDC User
    MockOIDCUser().inject_mocked_oidc_user(
        id="0000-0000-0000-0000",
        username="admin",
        roles=["g5-end-users", "g5-admin"]
    )