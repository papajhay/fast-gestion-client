from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


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
    
    
# ---------- Schéma de réponse----------

class ClientResponse(BaseModel):
    Mail: str
    Nom: str
    Prénom: str
    Commercial: str
    Chaleur: int
    Date_d_arrivée: Optional[str] = Field(None, alias="Date d'arrivée")
    Nombre_d_appel: int = Field(..., alias="Nombre d'appel")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    @field_validator("Date_d_arrivée", mode="before")
    @classmethod
    def format_date_arrivee(cls, value):
        if value is None:
            return None
        if isinstance(value, date):
            return value.strftime("%d/%m/%Y")
        if isinstance(value, str):
            try:
                d = date.fromisoformat(value)
                return d.strftime("%d/%m/%Y")
            except ValueError:
                return value
        return value