def extract_first_char(s: str):
    if s is None:
        raise ValueError("argument cannot be None")
    if not isinstance(s, str):
        raise TypeError("argument must be a string")
    if len(s) < 2:
        raise ValueError("argument must consist of 2 characters")
    return s[0]

try:
    extract_first_char(100)
except TypeError as ex:
    print(ex)

try:
    extract_first_char('s')
except ValueError as ex:
    print(ex)

from pydantic import validate_call, Field
from typing import Annotated

NonEmptyString = Annotated[str, Field(min_length=2)]

@validate_call
def extract_first_char(s:NonEmptyString) -> str:
    return s[0]

print(extract_first_char('as'))

try:
    extract_first_char(None)
except Exception as ex:
    print(ex)

try:
    extract_first_char("A")
except Exception as ex:
    print(ex)


from datetime import datetime
from typing import Any

import pytz
from dateutil.parser import parse

def make_utc(dt: datetime) -> datetime:
    print("make_utc called...")
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt
    
def parse_datetime(value: Any):
    print("parse_datetime called...")
    if isinstance(value, str):
        try:
            return parse(value)
        except Exception as ex:
            raise ValueError(str(ex))
    return value

from pydantic import BeforeValidator, AfterValidator

DatetimeUTC = Annotated[datetime, BeforeValidator(parse_datetime), AfterValidator(make_utc)]

@validate_call
def func(dt: DatetimeUTC):
    return dt.isoformat()

print(func("2024/5/22 3pm"))

# If your application already uses pydantic then go ahead with pydantic for validation,
# but if not, then only python might be better instead of adding dependency of pydantic.

def func(dt: datetime | str):
    try:
        dt = parse(dt)
    except Exception as ex:
        raise ValueError(str(ex))
    dt = make_utc(dt)
    return dt

print(func('2024/5/22 3pm'))