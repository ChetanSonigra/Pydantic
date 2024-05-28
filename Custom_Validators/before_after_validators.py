from pydantic import BaseModel, Field, field_validator
from datetime import datetime
import pytz
from dateutil.parser import parse
from typing import Any

class Model(BaseModel):
    dt: datetime

    @field_validator("dt", mode="before")
    @classmethod
    def parse_datetime(cls, value: Any):
        if isinstance(value, str):
            try:
                return parse(value)
            except Exception as ex:
                raise ValueError(str(ex))
        return value

    @field_validator("dt")
    @classmethod
    def make_utc(cls, dt: datetime) -> datetime:
        if dt.tzinfo is None:
            dt = pytz.utc.localize(dt)
        else:
            dt = dt.astimezone(pytz.utc)
        return dt
    
m = Model(dt="2020/1/1 3pm")
print(m)
m = Model(dt=100_000)
print(m)