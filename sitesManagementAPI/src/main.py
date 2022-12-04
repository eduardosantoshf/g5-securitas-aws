from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src.routers import users, alarms, properties, intrusions, cameras
from src.idp.idp import idp

app = FastAPI(title="Sites managment API", docs_url="/sites-man-api/docs", redoc_url=None)

origins = [
    "*",
]

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

idp.add_swagger_config(app)

@app.get("/sites-man-api")
def root():
    return RedirectResponse(url='/sites-man-api/docs')
