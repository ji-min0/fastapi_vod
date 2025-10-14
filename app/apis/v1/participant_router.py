import uuid

from fastapi import APIRouter

from app.dtos.create_participant_request import CreateParticipantRequest
from app.dtos.create_participant_response import CreateParticipantEdgedbResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/participants", tags=["Participant"])
# mysql_router = APIRouter(prefix="/v1/mysql/participants", tags=["Participant"])


@edgedb_router.post("", description="participant 를 생성합니다.")
async def api_create_participant_edgedb(
    create_participant_request: CreateParticipantRequest,
) -> CreateParticipantEdgedbResponse:
    return CreateParticipantEdgedbResponse(participant_id=uuid.uuid4(), participant_dates=[])


# @mysql_router.post("", description="participant 를 생성합니다.")
# async def api_create_participant_mysql(
#         create_participant_request: CreateParticipantRequest,
# ) -> CreateParticipantMysqlResponse:
#     return CreateParticipantMysqlResponse(participant_id=123, participant_dates=[])
