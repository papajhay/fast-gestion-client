from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    mail: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    nom: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    prenom: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    commercial: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    chaleur: Mapped[int] = mapped_column(
    Integer,
    nullable=False,
    )

    dateArrivee: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    nombreAppel: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )