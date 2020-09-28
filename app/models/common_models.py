from pydantic import BaseModel
from datetime import datetime


class RecordRequest(BaseModel):
    start_at: datetime
    end_at: datetime
    channel: str  # TODO change to enum
    title: str
    episode: int = None
    description: str = ""
