from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.routers import camera
from src.routers import intrusion
from dotenv import load_dotenv
import os
from src.database import Base, engine

app = FastAPI(title="Intrusion management API", docs_url="/intrusion-management-api/docs", redoc_url=None)

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

Base.metadata.create_all(bind=engine)


app.include_router(camera.router)
app.include_router(intrusion.router)

def configure():
    load_dotenv(os.path.join(os.getcwd(), "src/.env"))

@app.get("/intrusion-management-api")
def root():
    configure()
    return RedirectResponse(url='/intrusion-management-api/docs')


