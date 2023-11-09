from sqlalchemy.ext.asyncio import AsyncSession

from db.models.danger import DBDanger
from db.models.human import DBHuman
from db.repository.danger import DangerRepository


class DangerManager:

    @staticmethod
    async def get_danger(id_: int, session: AsyncSession):
        danger: DBDanger = await DangerRepository(session).get_danger_id(id_=id_)
        dangers: list[DBDanger] = await DangerRepository(session).get_dangers_except_danger_id(id_=id_)

        suspenders: list[DBHuman] = await DangerRepository(session).get_suspenders_short(ids=danger.suspenders)
        print(suspenders)
        return danger, dangers, suspenders

    @staticmethod
    async def get_dangers(session: AsyncSession):
        return await DangerRepository(session).get_all()
