from fastapi import APIRouter, Depends

from api.response.danger import DangerResponse, DangerResponseFactory, DangerListResponseFactory

from sqlalchemy.ext.asyncio import AsyncSession

from managers.danger import DangerManager
from server.depends import get_session

router = APIRouter(prefix='/danger')


@router.get("/all")
async def get_dangers(
        session: AsyncSession = Depends(get_session)
):
    dangers = await DangerManager.get_dangers(session)

    return DangerListResponseFactory.from_models(dangers)


@router.get('/{id}', response_model=DangerResponse)
async def get_danger(
        id_: int,
        session: AsyncSession = Depends(get_session),
):
    danger = await DangerManager.get_danger(id_=id_, session=session)

    return DangerResponseFactory.from_models(danger[0], danger[1], danger[2])



