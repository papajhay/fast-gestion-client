from fastapi import FastAPI

from app.database import Base, engine
from app.models.client import Client
from app.routers.clients import router as clients_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Gestion Clients API",
    version="1.0.0",
)


app.include_router(clients_router)


@app.get("/")
def root():
    return {
        "message": "API Gestion Clients"
    }