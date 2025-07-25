from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List

from . import Base
from .user import User, user_owns_steam_app_m2m

class SteamApp(Base):
    __tablename__ = "steam_app"
    app_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(100))
    required_age: Mapped[int] = mapped_column(Integer)
    is_free: Mapped[bool] = mapped_column(Boolean)
    supported_languages: Mapped[str] = mapped_column(Text)

    positive_reviews: Mapped[int] = mapped_column(Integer)
    negative_reviews: Mapped[int] = mapped_column(Integer)

    base_game: Mapped[int] = mapped_column(Integer, ForeignKey("steam_app.app_id"))

    dlc: Mapped[List["SteamApp"]] = relationship("SteamApp")
    owners: Mapped[List[User]] = relationship(secondary=user_owns_steam_app_m2m)