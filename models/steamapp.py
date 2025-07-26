from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List, Optional, TYPE_CHECKING

from . import Base
from .user import user_owns_steam_app_m2m

if TYPE_CHECKING:
    from . import User

class SteamApp(Base):
    __tablename__ = "steam_app"
    appid: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    required_age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_free: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    supported_languages: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    positive_reviews: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    negative_reviews: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    base_game: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("steam_app.appid"), nullable=True)

    dlc: Mapped[List["SteamApp"]] = relationship("SteamApp")
    owners: Mapped[List["User"]] = relationship(secondary=user_owns_steam_app_m2m)