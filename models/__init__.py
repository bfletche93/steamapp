from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .languages import Language
from .steamapp import SteamApp
from .achievements import Achievement, LocalizedAchievement
from .user import User