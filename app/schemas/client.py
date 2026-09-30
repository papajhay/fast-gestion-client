from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr


class ClientBase(BaseModel):
    mail: EmailStr
    nom: str
    prenom: str
    commercial: str
    chaleur: int
    dateArrivee: date
    nombreAppel: int = 0


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
    
class ClientPatch(BaseModel):
    mail: EmailStr | None = None
    nom: str | None = None
    prenom: str | None = None
    commercial: str | None = None
    chaleur: int | None = None
    dateArrivee: date | None = None
    nombreAppel: int | None = None