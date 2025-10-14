import datetime
import uuid

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG

# class ParticipantMysql(BaseModel):
#     model_config = FROZEN_CONFIG
#     id: int
#     date: datetime.date
#
#
# class CreateParticipantMysqlResponse(BaseModel):
#     model_config = FROZEN_CONFIG
#     participant_id: int
#     participant_dates: list[ParticipantMysql]


class ParticipantEdgedb(BaseModel):
    model_config = FROZEN_CONFIG
    id: uuid.UUID
    date: datetime.date


class CreateParticipantEdgedbResponse(BaseModel):
    model_config = FROZEN_CONFIG
    participant_id: uuid.UUID
    participant_dates: list[ParticipantEdgedb]
