import sqlalchemy.types as types

from db.models.base import BaseModel
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    ARRAY
)


class DBDanger(BaseModel):
    __tablename__ = "danger"

    name = Column(String, nullable=True)

    description = Column(String, nullable=True)

    shots = Column(ARRAY(String), nullable=True)

    suspenders = Column(ARRAY(Integer), nullable=True)

    danger_level = Column(Integer, nullable=False)

    status = Column(Integer, nullable=True, default=0)

    address = Column(String, nullable=False)

