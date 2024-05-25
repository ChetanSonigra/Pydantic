from pydantic import BaseModel, ValidationError, ConfigDict


class Model(BaseModel):
    field_1: int

m = Model(field_1=10, field_2=20)
print(m,m.model_dump(),m.model_fields_set)


class Model(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_1: int
    # class Config:
    #     extra='ignore'

m = Model(field_1=10, field_2=20)
print(m,m.model_dump(),m.model_fields_set)


class Model(BaseModel):
    model_config = ConfigDict(extra='allow')
    field_1: int
    # class Config:
    #     extra='allow'

m = Model(field_1=10, field_2=20)
print(m,m.model_dump(),m.model_fields_set)


class Model(BaseModel):
    model_config = ConfigDict(extra='forbid')
    field_1: int
    # class Config:
    #     extra='forbid'
try: 
    m = Model(field_1=10, field_2=20)
    print(m,m.model_dump(),m.model_fields_set)
except ValidationError as ex:
    print(ex)
