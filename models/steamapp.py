from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

class SteamApp(Base):
    __tablename__ = "steamapp"
    appid: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(100))
    required_age: Mapped[int] = mapped_column(Integer)
    is_free: Mapped[bool] = mapped_column(Boolean)
    supported_languages: Mapped[str] = mapped_column(Text)

    positive_reviews: Mapped[int] = mapped_column(Integer)
    negative_reviews: Mapped[int] = mapped_column(Integer)

    base_game: Mapped[int] = mapped_column(Integer, ForeignKey("steamapp.appid"))

    dlc = relationship("SteamApp")