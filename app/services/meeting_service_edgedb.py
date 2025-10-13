import uuid

from app.queries.meeting.create_meeting_async_edgeql import (
    CreateMeetingResult,
    create_meeting,
)
from app.utils.base62 import Base62
from app.utils.edge import edgedb_client


async def service_create_meeting_edgedb() -> CreateMeetingResult:
    return await create_meeting(
        executor=edgedb_client,
        url_code=Base62.encode(uuid.uuid4().int),
    )
