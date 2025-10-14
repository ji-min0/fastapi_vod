from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG


class CreateParticipantRequest(BaseModel):
    model_config = FROZEN_CONFIG

    meeting_url_code: str
    name: str
