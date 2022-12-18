from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, HTTPException, status
from fastapi_keycloak import OIDCUser
from jose import ExpiredSignatureError

from sqlalchemy.orm import Session
import src.db.repositories.properties_crud as properties_crud, src.models.schemas as schemas
from src.routers import users, alarms, properties, intrusions, cameras
from src.db.database import get_db
from src.idp.idp import idp

origins = [
    "*",
]

app = FastAPI(title="Sites managment API", docs_url="/sites-man-api/docs", redoc_url=None,\
                openapi_url="/sites-man-api/openapi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(alarms.router)
app.include_router(properties.router)
app.include_router(cameras.router)
app.include_router(intrusions.router)

#idp.add_swagger_config(app)

@app.get("/sites-man-api")
def root():
    return RedirectResponse(url='/sites-man-api/docs')

@app.get("/sites-man-api/callback")
def callback(db: Session = Depends(get_db), user: OIDCUser = Depends(idp.get_current_user(required_roles=['g5-end-users']))):

    try:
        idp.get_user(user_id=user.sub, query=None)
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Signature expired")
    except: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {owner_id} not found")

    prpty = schemas.PropertyCreate(address=f"{user.sub}'address")

    query = properties_crud.create_property(property=prpty, owner_id=user.sub, db=db)
    
    if query is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Property already registred')

    return RedirectResponse(url='http://securitas-lb-1725284772.eu-west-3.elb.amazonaws.com:80/')
