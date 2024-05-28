from pydantic import ValidationError,Field, BaseModel, field_validator, ValidationInfo

from datetime import datetime

class Model(BaseModel):
    field1: int
    field2: list[int]
    field3: str
    field4: list[str]

    @field_validator('field3')
    @classmethod
    def validator_field3(cls,value,info: ValidationInfo):
        print(info)
        print(value)
        return value
    
m = Model(field1=4, field2=[2,3,4],field3='slj',field4=['sf'])
print(m)

try:
    Model(field1=4,field2=['sd',4,5],field3='d',field4=['s'])
except ValidationError as ex:
    print(ex)


from typing import Annotated, Any

import pytz
from dateutil.parser import parse
from pydantic import AfterValidator, BeforeValidator

def parse_datetime(value: Any):
    if isinstance(value, str):
        try:
            return parse(value)
        except Exception as ex:
            raise ValueError(str(ex))
    return value


def make_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt

DateTimeUTC = Annotated[datetime, BeforeValidator(parse_datetime), AfterValidator(make_utc)]

class Model(BaseModel):
    start_dt: DateTimeUTC
    end_dt: DateTimeUTC

    @field_validator('end_dt')
    @classmethod
    def end_date_validator(cls,dt, data: ValidationInfo):
        value = data.data
        if 'start_dt' in value:
            if dt<value['start_dt']:
                raise ValueError('End date can not be before start date.')
        return dt
    
m = Model(start_dt="2024/5/26",end_dt="2024/5/27")
print(m)

try:
    m = Model(start_dt="2024/5/26", end_dt="2024/5/25")
except ValidationError as ex:
    print(ex)

