from sqlalchemy import func,ForeignKey,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship,Mapped,mapped_column
from typing import List
from . import Base
from .association import game_user

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(unique=True)
    created_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdate=func.now())

    games:Mapped[List["Game"]]=relationship(secondary=game_user,back_populates="users",passive_deletes=True,)#,cascade="all,delete"