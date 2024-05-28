from pydantic import BaseModel, ValidationError, ConfigDict, Field, field_validator
from datetime import datetime,UTC
import pytz

class Model(BaseModel):
    number: int = Field(gt=0,lt=10)

    @field_validator('number')
    @classmethod
    def validate_even(cls,value):
        print('running custom validator')
        if value%2==0:
            return value
        raise ValueError('Value must be even.')
        # value += 1
        # return value
    
try:
    m = Model(number=3)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    dt: datetime

    @field_validator('dt')
    @classmethod
    def make_utc(cls,dt: datetime):
        if dt.tzinfo is None:
            dt = pytz.utc.localize(dt)
        else:
            dt = dt.astimezone(pytz.utc)
        return dt
    
print(Model(dt="2024-05-27T03:00:00"))

eastern = pytz.timezone('US/Eastern')
dt = eastern.localize(datetime(2024,5,27,3,0,0))
print(Model(dt=dt))

# sequence of after validators: top to bottom

class Model(BaseModel):
    number: int

    @field_validator('number')
    @classmethod
    def validator_1(cls,value):
        print('validator 1')
        return value
    @field_validator('number')
    @classmethod
    def validator_2(cls,value):
        print('validator 2')
        return value
    @field_validator('number')
    @classmethod
    def validator_3(cls,value):
        print('validator 3')
        return value
    
m = Model(number=1)


class Model(BaseModel):
    unit_cost: float
    unit_price: float

    @field_validator('*')
    @classmethod
    def round_2(cls,value):
        value = round(value,2)
        return value

m = Model(unit_cost=2.434343,unit_price=4.323423)
print(m)