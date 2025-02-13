from pydantic import BaseModel
from typing import List

class AvailabilityCreate(BaseModel):
    user_id: int
    date: str
    start_time: str
    end_time: str

class EventCreate(BaseModel):
    user_id: int
    date: str
    start_time: str
    end_time: str

class AvailabilityRequest(BaseModel):
    user_ids: List[int]
    start_date: str
    end_date: str
    timezone: str
