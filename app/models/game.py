from sqlalchemy import Integer,String,func,DateTime
from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import List
from datetime import datetime
from . import Base
from .association import game_user
#from review import Review

class Game(Base):
    __tablename__="games"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(255))
    genre:Mapped[str]=mapped_column(String(100))
    platform:Mapped[str]=mapped_column(String(100))
    price:Mapped[int]
    created_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now(),onupdate=func.now())

    reviews:Mapped[List["Review"]]=relationship(back_populates="game",cascade="all, delete-orphan")
    users:Mapped[List["User"]]=relationship(secondary=game_user,back_populates="games",passive_deletes=True)