import datetime
from typing import Optional

from sqlalchemy import select, desc, and_
from sqlalchemy.orm import joinedload

from db.models.danger import DBDanger
from db.models.human import DBHuman
from db.repository.base import BaseRepository


class DangerRepository(BaseRepository):

    async def get_danger_id(self, id_: int) -> DBDanger:
        query = (
            select(DBDanger)
            .select_from(DBDanger)
            .where(
                DBDanger.id == id_
            )
            .limit(1)
        )

        return await self.one_val(query)

    async def get_dangers_except_danger_id(self, id_: int) -> list[DBDanger]:
        query = (
            select(DBDanger)
            .select_from(DBDanger)
            .where(
                DBDanger.id != id_
            )
            .limit(1)
        )

        return await self.all_ones(query)

    async def get_suspenders_short(self, ids: list[int]):
        query = (
            select(DBHuman)
            .select_from(DBHuman)
            .where(
                DBHuman.id.in_(ids)
            )
        )

        return await self.all_ones(query)

    async def get_all(self):
        query = (
            select(DBDanger)
            .select_from(DBDanger)
        )

        return await self.all_ones(query)

