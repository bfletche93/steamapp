from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List, TYPE_CHECKING

from app import db

from . import Base

if TYPE_CHECKING:
    from .steamapp import SteamApp

user_owns_steam_app_m2m = db.Table(
    "user_owns_steam_app_m2m",
    Column("user_id", ForeignKey("user.user_id"), primary_key=True),
    Column("app_id", ForeignKey("steam_app.app_id"), primary_key=True)
)

class User(Base):
    __tablename__ = "user"
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    persona_name: Mapped[str] = mapped_column(String(50))

    owned_games: Mapped[List["SteamApp"]] = relationship(secondary=user_owns_steam_app_m2m)
