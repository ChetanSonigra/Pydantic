from pydantic import Field, BaseModel, BeforeValidator, \
    AfterValidator, ValidationError
from datetime import datetime, UTC
from dateutil.parser import parse
import pytz
from typing import Any, Annotated, TypeVar


def parse_datetime(value: Any) -> datetime:
    if isinstance(value,str):
        try:
            value = parse(value)
        except Exception as ex:
            raise ValueError(str(ex))
        return value


DateTime = Annotated[datetime,BeforeValidator(parse_datetime)]
class Model(BaseModel):
    dt: DateTime

m = Model(dt="2024/5/24 8:00 PM")
print(m)


def make_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt
DateTimeUTC = Annotated[datetime,AfterValidator(make_utc), BeforeValidator(parse_datetime)]
#  you can put as many validators as you want.

class Model(BaseModel):
    dt: DateTimeUTC

m = Model(dt="2024-5-23 2:00 pm")
print(m)


def are_elements_unique(values: list[Any]) -> list[Any]:
    unique_elements = []
    for x in values:
        if x in unique_elements:
            raise ValueError("Elements must be unique.")
        unique_elements.append(x)
    return values

T = TypeVar('T')
UniqueList = Annotated[list[T],AfterValidator(are_elements_unique)]
# can add other things as well, like Field(gt=0,le=5)

class Model(BaseModel):
    numbers: UniqueList[int]
    strings: UniqueList[str]

m  = Model(numbers=[1,2,4],strings=['a','b'])
print(m)

try:
    Model(numbers=['1',3,4],strings=[3,5])
except ValidationError as ex:
    print(ex)