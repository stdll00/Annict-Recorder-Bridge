from pydantic import BaseModel
from datetime import datetime

from enum import Enum


class RecordStatus(Enum):
    RESERVED = "RESERVED"
    DUPLICATED = "DUPLICATED"
    CONFLICT = "CONFLICT"
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"


class RecordRequest(BaseModel):
    start_at: datetime
    end_at: datetime
    channel: str  # TODO change to enum
    title: str
    episode_title: str = ""
    episode: int = None
    description: str = ""
