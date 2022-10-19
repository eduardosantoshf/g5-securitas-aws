from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def root():
    return RedirectResponse(url='/docs')
