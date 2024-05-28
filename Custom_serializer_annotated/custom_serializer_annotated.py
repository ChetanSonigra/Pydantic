from datetime import datetime
from typing import Annotated, Any

import pytz
from dateutil.parser import parse

from pydantic import BaseModel, AfterValidator, BeforeValidator, PlainSerializer


def make_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt
    
def parse_datetime(value: Any):
    if isinstance(value, str):
        try:
            return parse(value)
        except Exception as ex:
            raise ValueError(str(ex))
    return value


DateTimeUTC = Annotated[datetime, BeforeValidator(parse_datetime), AfterValidator(make_utc)]

class Model(BaseModel):
    dt: DateTimeUTC

def dt_json_serializer(dt: datetime) -> str:
    return dt.strftime("%Y/%m/%d %I:%M %p UTC")

print(dt_json_serializer(datetime(2020,1,1,15,0,0)))

DateTimeUTC = Annotated[datetime,
                        BeforeValidator(parse_datetime),
                        AfterValidator(make_utc),
                        PlainSerializer(dt_json_serializer,when_used='json-unless-none')]

class Model(BaseModel):
    dt: DateTimeUTC

m = Model(dt="2024/5/23 3 PM")

print(m)
print(m.model_dump())
print(m.model_dump_json())
