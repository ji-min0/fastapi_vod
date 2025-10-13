from datetime import datetime

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.dtos.update_meeting_request import UpdateMeetingDateRangeRequest
from app.services.meeting_service_edgedb import (
    service_create_meeting_edgedb,
    service_get_meeting_edgedb,
)

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
# mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원래는 어떤 DB 를 쓰는지 URL 에 적을 필요 없습니다!
# 강의에서만 이렇게 합니다!
# 실전에서는 db 이름을 url 에 넣지 마세요


@edgedb_router.post("", description="meeting 을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_edgedb()).url_code)


# @mysql_router.post("", description="meeting 을 생성합니다.")
# async def api_create_meeting_mysql() -> CreateMeetingResponse:
#     return CreateMeetingResponse(url_code=(await service_create_meeting_mysql()).url_code)


@edgedb_router.get(
    "/{meeting_url_code}",  # path variable
    description="meeting 을 조회합니다.",
)
async def api_get_meeting_edgedb(meeting_url_code: str) -> GetMeetingResponse:
    meeting = await service_get_meeting_edgedb(meeting_url_code)
    if meeting is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    return GetMeetingResponse(
        url_code=meeting.url_code,
        end_date=datetime.now().date(),
        start_date=datetime.now().date(),
        title="test",
        location="test",
    )


# @mysql_router.get(
#     "/{meeting_url_code}",  # path variable
#     description="meeting 을 조회합니다.",
# )
# async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
#     meeting = await service_get_meeting_mysql(meeting_url_code)
#     if meeting is None:
#         raise HTTPException(
#             status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
#         )
#     return GetMeetingResponse(
#         url_code=meeting.url_code,
#         start_date=datetime.now().date(),
#         end_date=datetime.now().date(),
#         title="test",
#         location="test",
#     )


@edgedb_router.patch("/{meeting_url_code}/date_range", description="meeting 의 날짜 range 를 설정합니다.")
async def api_update_meeting_date_range_edgedb(
    meeting_url_code: str, update_meeting_date_range_request: UpdateMeetingDateRangeRequest
) -> GetMeetingResponse:
    return GetMeetingResponse(
        url_code="abc",
        start_date=datetime.now().date(),
        end_date=datetime.now().date(),
        title="test",
        location="test",
    )


# @mysql_router.patch("/{meeting_url_code}/date_range", description="meeting 의 날짜 range 를 설정합니다.")
# async def api_update_meeting_date_range_mysql(
#     meeting_url_code: str, update_meeting_date_range_request: UpdateMeetingDateRangeRequest
# ) -> GetMeetingResponse:
#     return GetMeetingResponse(
#         url_code="abc",
#         start_date=datetime.now().date(),
#         end_date=datetime.now().date(),
#         title="test",
#         location="test",
#     )
