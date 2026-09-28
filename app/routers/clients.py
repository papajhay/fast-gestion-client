from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientResponse, ClientUpdate, ClientPatch


router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
)


@router.post("/", response_model=ClientResponse, status_code=201)
def create_client(
    client: ClientCreate,
    db: Session = Depends(get_db),
):
    existing_client = (
        db.query(Client)
        .filter(Client.mail == client.mail)
        .first()
    )

    if existing_client:
        raise HTTPException(
            status_code=400,
            detail="Un client avec cet email existe déjà.",
        )

    new_client = Client(**client.model_dump())

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client


@router.get("/", response_model=list[ClientResponse])
def get_clients(
    db: Session = Depends(get_db),
):
    return db.query(Client).all()


@router.get("/{id}", response_model=ClientResponse)
def get_client(
    id: int,
    db: Session = Depends(get_db),
):
    client = (
        db.query(Client)
        .filter(Client.id == id)
        .first()
    )

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Client introuvable.",
        )

    return client


@router.put("/{id}", response_model=ClientResponse)
def update_client(
    id: int,
    client_data: ClientUpdate,
    db: Session = Depends(get_db),
):
    client = (
        db.query(Client)
        .filter(Client.id == id)
        .first()
    )

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Client introuvable.",
        )

    # Vérifier que le nouvel email n'est pas déjà utilisé
    existing_client = (
        db.query(Client)
        .filter(
            Client.mail == client_data.mail,
            Client.id != id,
        )
        .first()
    )

    if existing_client:
        raise HTTPException(
            status_code=400,
            detail="Cet email est déjà utilisé par un autre client.",
        )

    # Mise à jour des champs
    client.mail = client_data.mail
    client.nom = client_data.nom
    client.prenom = client_data.prenom
    client.commercial = client_data.commercial
    client.chaleur = client_data.chaleur
    client.date_arrivee = client_data.date_arrivee
    client.nombre_appel = client_data.nombre_appel

    db.commit()
    db.refresh(client)

    return client


@router.delete("/{id}", status_code=204)
def delete_client(
    id: int,
    db: Session = Depends(get_db),
):
    client = (
        db.query(Client)
        .filter(Client.id == id)
        .first()
    )

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Client introuvable.",
        )

    db.delete(client)
    db.commit()
    
    
@router.patch("/{id}", response_model=ClientResponse)
def patch_client(
    id: int,
    client_data: ClientPatch,
    db: Session = Depends(get_db),
):
    client = (
        db.query(Client)
        .filter(Client.id == id)
        .first()
    )

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Client introuvable.",
        )

    data = client_data.model_dump(exclude_unset=True)

    if "mail" in data:
        existing_client = (
            db.query(Client)
            .filter(
                Client.mail == data["mail"],
                Client.id != id,
            )
            .first()
        )

        if existing_client:
            raise HTTPException(
                status_code=400,
                detail="Cet email est déjà utilisé par un autre client.",
            )

    for field, value in data.items():
        setattr(client, field, value)

    db.commit()
    db.refresh(client)

    return client