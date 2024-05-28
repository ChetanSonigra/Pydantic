from pydantic import ValidationError, Field, BaseModel, field_validator
from datetime import datetime
from dateutil import parser

# we want to allow dt="2020/1/1 3:00pm" and (dt="Jan 1, 2020 3:00pm") as date as well in our model.

class Model(BaseModel):
    dt: datetime

    @field_validator('dt', mode='before')
    @classmethod
    def date_validator(cls,value):
        if isinstance(value,str):
            try:
                value = parser.parse(value)
            except Exception as ex:
                raise ValueError(str(ex))
        return value
    
m = Model(dt="2020/1/1 3:00pm")
print(m)
m = Model(dt="Jan 1, 2020 3:00pm")
print(m)

try:
    Model(dt=[1,3,4])
except ValidationError as ex:
    print(ex)


# Sequence of before validators: bottom to up

class Model(BaseModel):
    n: int

    @field_validator('n',mode='before')
    @classmethod
    def validator_1(cls,value):
        print('validator 1')
        return value
    @field_validator('n',mode='before')
    @classmethod
    def validator_2(cls,value):
        print('validator 2')
        return value
    @field_validator('n',mode='before')
    @classmethod
    def validator_3(cls,value):
        print('validator 3')
        return value
    
m = Model(n=2)