from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass



from .game import Game
from .review import Review
from .user import User