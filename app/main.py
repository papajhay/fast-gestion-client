from fastapi import FastAPI

from app.database import Base, engine
from app import models  # noqa: F401 - register all models before create_all
from app.routers import auth, clients


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Gestion Clients API",
    version="1.0.0",
)


app.include_router(auth.router)
app.include_router(clients.router)


@app.get("/")
def root():
    return {
        "message": "API Gestion Clients"
    }
