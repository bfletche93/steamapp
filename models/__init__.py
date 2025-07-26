from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .languages import Language
from .steamapp import SteamApp
from .achievements import Achievement
from .user import User