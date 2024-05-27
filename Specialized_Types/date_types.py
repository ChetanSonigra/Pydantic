from pydantic import (
    BaseModel,
    ValidationError,
    ConfigDict,
    PastDate,
    PastDatetime,
    NaiveDatetime,
    AwareDatetime
)
from datetime import datetime,timedelta
import pytz

local_one_hour_ago = datetime.now() - timedelta(hours=1)
utc_one_hour_ago = local_one_hour_ago.astimezone(pytz.utc)
local_one_hour_after = datetime.now() + timedelta(hours=1)

class Model(BaseModel):
    dt: PastDatetime
try:
    m = Model(dt=local_one_hour_after)
    print(m)
except ValidationError as ex:
    print(ex)

m = Model(dt=local_one_hour_ago)
print(m)


class Model(BaseModel):
    dt: NaiveDatetime

m = Model(dt=local_one_hour_ago)
print(m)

try:
    m = Model(dt=utc_one_hour_ago)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    dt: AwareDatetime

m = Model(dt=utc_one_hour_ago)
print(m)

try:
    m = Model(dt=local_one_hour_after)
except ValidationError as ex:
    print(ex)



