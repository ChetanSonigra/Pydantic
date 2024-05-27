from pydantic import BaseModel, ConfigDict, Field, ValidationError

from datetime import datetime, UTC
import time

def log(text: str, dt: datetime = datetime.now(UTC)):
    print(f"{dt.isoformat()}",text)

log('line1',datetime(2024,5,27,10,30))
log('line2')
time.sleep(5)
log('line3')
# line2 and line3 gives same time because default values are
# calculated only once when function is compiled.

class Model(BaseModel):
    elements: list[int] = []

m = Model()
print(m)
m.elements.append(1)

m2 = Model()
print(m2.elements)
# pydantic handles this situation with list by creating deep copy.


class Log(BaseModel):
    dt: datetime = Field(default_factory=lambda: datetime.now(UTC))
    msg: str

print(Log(msg='line1'))
time.sleep(5)
print(Log(msg="line2"))
