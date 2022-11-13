from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.routers import camera
from dotenv import load_dotenv
import os


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

app.include_router(camera.router)

def configure():
    load_dotenv(os.path.join(os.getcwd(), "src/.env"))

@app.get("/intrusion-management-api")
def root():
    configure()
    return RedirectResponse(url='/intrusion-management-api/docs')