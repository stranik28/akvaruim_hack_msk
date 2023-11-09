from api.response.base import ResponseBase
from pydantic import Field

from db.models.danger import DBDanger
from db.models.human import DBHuman
from datetime import datetime


class DangersShort(ResponseBase):
    id: int = Field(...)
    danger_count: int = Field(...)
    time: datetime = Field(...)
    danger_level: int = Field(...)


class Shots(ResponseBase):
    name: str = Field(...)
    time: datetime = Field(...)
    shot: str = Field(...)


class SuspenderShort(ResponseBase):
    id: int = Field(...)
    photo: str = Field(...)


class DangerResponse(ResponseBase):
    dangers: list[DangersShort] = Field(...)

    shots: list[Shots] = Field(...)

    description: str = Field(...)

    title: str = Field(...)

    suspenders: list[SuspenderShort] = Field(...)


class DangerListResponse(ResponseBase):
    id: int = Field(...)

    number: str = Field(...)

    address: str = Field(...)

    reaction: str = Field(...)

    date: datetime = Field(...)

    status: int = Field(...)


class DangerResponseFactory:
    @staticmethod
    def from_models_danger(models: list[DBDanger]) -> list[DangersShort]:
        return [DangersShort(id=i.id, danger_count=1, time=i.created_at, danger_level=i.danger_level) for i in models]

    @staticmethod
    def from_models_suspender(models: list[DBHuman]) -> list[SuspenderShort]:
        return [SuspenderShort(id=i.id, photo=i.photo) for i in models]

    @staticmethod
    def from_models_shots(shots, time):
        return [Shots(name="Снимок нарушителя", time=time, shot=shot) for shot in shots]

    @classmethod
    def from_models(cls, danger: DBDanger, dangers: list[DBDanger], suspenders: list[DBHuman]) -> DangerResponse:
        return DangerResponse(
            description=danger.description,
            title=danger.name,
            dangers=cls.from_models_danger(dangers),
            suspenders=cls.from_models_suspender(suspenders),
            shots=cls.from_models_shots(danger.shots, danger.created_at)
        )


class DangerListResponseFactory:

    @staticmethod
    def from_model(danger: DBDanger) -> DangerListResponse:
        return DangerListResponse(
            id=danger.id,
            number=danger.name,
            address=danger.address,
            reaction="In developing...",
            date=danger.created_at,
            status=danger.status or 0
        )

    @classmethod
    def from_models(cls, dangers: list[DBDanger]) -> list[DangerListResponse]:
        return [cls.from_model(danger) for danger in dangers]