from sqlalchemy import Integer,String,func,ForeignKey,DateTime
from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import List
from datetime import datetime
from . import Base
#from game import Game

class Review(Base):
    __tablename__="reviews"
    id:Mapped[int]=mapped_column(primary_key=True)
    score:Mapped[int]
    comment:Mapped[str]
    game_id:Mapped[int]=mapped_column(ForeignKey("games.id"))
    created_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now(),onupdate=func.now())

    game:Mapped["Game"]=relationship(back_populates="reviews")