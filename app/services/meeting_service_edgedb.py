import uuid
from datetime import date

from app.queries.meeting.create_meeting_async_edgeql import (
    CreateMeetingResult,
    create_meeting,
)
from app.queries.meeting.get_meeting_by_url_code_async_edgeql import (
    get_meeting_by_url_code,
)
from app.queries.meeting.models import FullMeeting
from app.queries.meeting.update_meeting_location_async_edgeql import (
    UpdateMeetingLocationResult,
    update_meeting_location,
)
from app.queries.meeting.update_meeting_start_end_async_edgeql import (
    update_meeting_start_end,
)
from app.queries.meeting.update_meeting_title_async_edgeql import (
    UpdateMeetingTitleResult,
    update_meeting_title,
)
from app.utils.base62 import Base62
from app.utils.edge import edgedb_client


async def service_create_meeting_edgedb() -> CreateMeetingResult:
    return await create_meeting(
        executor=edgedb_client,
        url_code=Base62.encode(uuid.uuid4().int),
    )


async def service_get_meeting_edgedb(meeting_url_code: str) -> FullMeeting | None:
    return await get_meeting_by_url_code(edgedb_client, url_code=meeting_url_code)


async def service_update_meeting_date_range_edgedb(
    meeting_url_code: str, start_date: date, end_date: date
) -> FullMeeting | None:
    return await update_meeting_start_end(
        edgedb_client, url_code=meeting_url_code, start_date=start_date, end_date=end_date
    )


async def service_update_meeting_location_edgedb(
    meeting_url_code: str, location: str
) -> UpdateMeetingLocationResult | None:
    return await update_meeting_location(
        edgedb_client,
        url_code=meeting_url_code,
        location=location,
    )


async def service_update_meeting_title_edgedb(meeting_url_code: str, title: str) -> UpdateMeetingTitleResult | None:
    return await update_meeting_title(
        edgedb_client,
        url_code=meeting_url_code,
        title=title,
    )
