from pydantic import BaseModel, ConfigDict,ValidationError

class Model(BaseModel):
    field: str

try:
    m = Model(field=1.0)
    print(m)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)  # only works in lax mode.
    field: str

try:
    m = Model(field=1.0)
    print(m)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True,strict=True)  # only works in lax mode.
    field: str

try:
    m = Model(field=1.0)
    print(m)
except ValidationError as ex:
    print(ex)
