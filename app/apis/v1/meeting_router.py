from fastapi import APIRouter, HTTPException
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_CONTENT,
)

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.dtos.update_meeting_request import (
    MEETING_DATE_MAX_RANGE,
    UpdateMeetingDateRangeRequest,
    UpdateMeetingLocationRequest,
    UpdateMeetingTitleRequest,
)
from app.services.meeting_service_edgedb import (
    service_create_meeting_edgedb,
    service_get_meeting_edgedb,
    service_update_meeting_date_range_edgedb,
    service_update_meeting_location_edgedb,
    service_update_meeting_title_edgedb,
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
        end_date=meeting.end_date,
        start_date=meeting.start_date,
        title=meeting.title,
        location=meeting.location,
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
    if update_meeting_date_range_request.exceeds_max_range():
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_CONTENT,
            detail=f"start {update_meeting_date_range_request.start_date} and end {update_meeting_date_range_request.end_date} should be within {MEETING_DATE_MAX_RANGE.days} days",
        )
    meeting_before_update = await service_get_meeting_edgedb(meeting_url_code)
    if meeting_before_update is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    if meeting_before_update.start_date or meeting_before_update.end_date:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_CONTENT,
            detail=f"meeting: {meeting_url_code} start: {meeting_before_update.start_date} end: {meeting_before_update.end_date} are already set",
        )
    meeting_after_update = await service_update_meeting_date_range_edgedb(
        meeting_url_code, update_meeting_date_range_request.start_date, update_meeting_date_range_request.end_date
    )
    assert meeting_after_update  # meeting 이 있었으므로 (삭제 기능은 없으므로) result 는 무조건 있습니다.
    return GetMeetingResponse(
        url_code=meeting_after_update.url_code,
        end_date=meeting_after_update.end_date,
        start_date=meeting_after_update.start_date,
        title=meeting_after_update.title,
        location=meeting_after_update.location,
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


@edgedb_router.patch(
    "/{meeting_url_code}/title",
    description="meeting 의 title 을 설정합니다.",
    status_code=HTTP_204_NO_CONTENT,
)
async def api_update_meeting_title_edgedb(
    meeting_url_code: str, update_meeting_title_request: UpdateMeetingTitleRequest
) -> None:
    updated = await service_update_meeting_title_edgedb(meeting_url_code, title=update_meeting_title_request.title)
    if not updated:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    return None


# @mysql_router.patch(
#     "/{meeting_url_code}/title",
#     description="meeting 의 title 을 설정합니다.",
#     status_code=HTTP_204_NO_CONTENT,
# )
# async def api_update_meeting_title_mysql(
#     meeting_url_code: str, update_meeting_title_request: UpdateMeetingTitleRequest
# ) -> None:
#     return None


@edgedb_router.patch(
    "/{meeting_url_code}/location",
    description="meeting 의 location 을 설정합니다.",
    status_code=HTTP_204_NO_CONTENT,
)
async def api_update_meeting_location_edgedb(
    meeting_url_code: str, update_meeting_location_request: UpdateMeetingLocationRequest
) -> None:
    updated = await service_update_meeting_location_edgedb(
        meeting_url_code, location=update_meeting_location_request.location
    )
    if not updated:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    return None


# @mysql_router.patch(
#     "/{meeting_url_code}/location",
#     description="meeting 의 location 을 설정합니다.",
#     status_code=HTTP_204_NO_CONTENT,
# )
# async def api_update_meeting_location_mysql(
#     meeting_url_code: str, update_meeting__location_request: UpdateMeetingLocationRequest
# ) -> None:
#     return None
