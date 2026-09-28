from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr


class ClientBase(BaseModel):
    mail: EmailStr
    nom: str
    prenom: str
    commercial: str
    chaleur: int
    date_arrivee: date
    nombre_appel: int = 0


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
    date_arrivee: date | None = None
    nombre_appel: int | None = None