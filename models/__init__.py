from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .steamapp import SteamApp