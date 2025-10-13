import dataclasses
import uuid


@dataclasses.dataclass(frozen=True)
class FullMeeting:
    id: uuid.UUID
    url_code: str
