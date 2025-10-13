import uuid

from app.queries.meeting.create_meeting_async_edgeql import (
    CreateMeetingResult,
    create_meeting,
)
from app.queries.meeting.get_meeting_by_url_code_async_edgeql import (
    get_meeting_by_url_code,
)
from app.queries.meeting.models import FullMeeting
from app.utils.base62 import Base62
from app.utils.edge import edgedb_client


async def service_create_meeting_edgedb() -> CreateMeetingResult:
    return await create_meeting(
        executor=edgedb_client,
        url_code=Base62.encode(uuid.uuid4().int),
    )


async def service_get_meeting_edgedb(meeting_url_code: str) -> FullMeeting | None:
    return await get_meeting_by_url_code(edgedb_client, url_code=meeting_url_code)
