from sqlalchemy import (ForeignKey, ForeignKeyConstraint, Float, Integer,
                        String, Text)
from sqlalchemy.orm import Mapped, mapped_column

from . import Base

class Achievement(Base):
    __tablename__ = "achievement"
    api_name: Mapped[str] = mapped_column(String(50), primary_key=True)
    app_id: Mapped[int] = mapped_column(Integer, ForeignKey("steam_app.app_id"), primary_key=True)
    percent: Mapped[float] = mapped_column(Float)
    type: Mapped[str] = mapped_column(String)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
        "polymorphic_on": "type"
    }


class LocalizedAchievement(Achievement):
    __tablename__ = "localized_achievement"
    api_name: Mapped[str] = mapped_column(String(50), primary_key=True)
    app_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    language_id: Mapped[str] = mapped_column(String(2),
                                             ForeignKey("language.web_api_language_code"),
                                             primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__
    }
    __table_args__ = (
        ForeignKeyConstraint(
            ["api_name", "app_id"],
            ["achievement.api_name", "achievement.app_id"]
        ),
    )