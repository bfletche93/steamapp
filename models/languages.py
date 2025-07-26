from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from . import Base

class Language(Base):
    __tablename__ = "language"

    english_name: Mapped[str] = mapped_column(String(50))
    api_language_code: Mapped[str] = mapped_column(String(50))
    web_api_language_code: Mapped[str] = mapped_column(String(2), primary_key=True)