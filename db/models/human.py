from db.models.base import BaseModel
from sqlalchemy import (
    Column,
    Text,
    Integer,
    String
)


class DBHuman(BaseModel):
    __tablename__ = "human"

    first_name = Column(Text, nullable=True)
    last_name = Column(Text, nullable=True)
    middle_name = Column(Text, nullable=True)

    photo = Column(String, nullable=True)

    danger_level = Column(Integer, nullable=True)
