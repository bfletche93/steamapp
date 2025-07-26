from sqlalchemy import (Boolean, Column, ForeignKey, ForeignKeyConstraint,
                        Integer, String)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import Set, TYPE_CHECKING

from app import db

from . import Base

if TYPE_CHECKING:
    from . import Achievement, SteamApp

user_owns_steam_app_m2m = db.Table(
    "user_owns_steam_app_m2m",
    Column("user_id", ForeignKey("user.user_id"), primary_key=True),
    Column("appid", ForeignKey("steam_app.appid"), primary_key=True)
)

class User(Base):
    __tablename__ = "user"
    user_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    persona_name: Mapped[str] = mapped_column(String(50), nullable=True)

    owned_games: Mapped[Set["SteamApp"]] = relationship(secondary=user_owns_steam_app_m2m,
                                                         back_populates="owners")

class UserAchievementAssociation(Base):
    __tablename__ = "user_achievement_association"
    user_id: Mapped[str] = mapped_column(String(50), ForeignKey("user.user_id"), primary_key=True)
    appid: Mapped[int] = mapped_column(Integer, primary_key=True)
    api_name: Mapped[str] = mapped_column(String(50), primary_key=True)

    achieved: Mapped[bool] = mapped_column(Boolean, default=False)
    unlock_time: Mapped[int] = mapped_column(Integer, default=None, nullable=True)

    user: Mapped["User"] = relationship()
    achievement: Mapped["Achievement"] = relationship()

    __table_args__ = (
        ForeignKeyConstraint(
            ["appid", "api_name"],
            ["achievement.appid", "achievement.api_name"]
        ),
    )