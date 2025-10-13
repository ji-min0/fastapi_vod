import dataclasses
import uuid
from datetime import date


@dataclasses.dataclass(frozen=True)
class FullMeeting:
    id: uuid.UUID
    url_code: str
    start_date: date | None
    end_date: date | None
    location: str
    title: str
