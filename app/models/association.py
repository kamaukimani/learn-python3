from sqlalchemy import Table,Column,Table,ForeignKey
from . import Base
game_user=Table(
    "game_users",
    Base.metadata,
    Column("game_id",ForeignKey("games.id",ondelete="CASCADE"),primary_key=True),
    Column("user_id",ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
)