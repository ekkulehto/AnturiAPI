from typing import Optional
from sqlmodel import Field, SQLModel

from ..models import SensorStatus

class SensorUpdate(SQLModel):
    name: Optional[str] = Field(default=None, description='New name for the sensor. If omitted, the name is not changed.')
    segment_id: Optional[int] = Field(default=None, description='New segment ID the sensor belongs to. If omitted, the segment is not changed.')

class SensorStatusUpdate(SQLModel):
    status: SensorStatus