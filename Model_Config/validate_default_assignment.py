from pydantic import BaseModel, ValidationError, ConfigDict

class Model(BaseModel):
    x: int = None
    y: str = 'ABC'

try:
    m = Model()
    print(m)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    model_config = ConfigDict(validate_default=True)
    x: int = None
    y: str = 'ABC'

try:
    m = Model()
    print(m)
except ValidationError as ex:
    print(ex)



class Model(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    x: int = None
    y: str = 'ABC'

try:
    m = Model()
    print(m)
    m.x= 'dsfkjs'
    print(m)
except ValidationError as ex:
    print(ex)
