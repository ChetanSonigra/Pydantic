from pydantic import BaseModel, ConfigDict, Field, ValidationError

# strict, validate_default, frozen, include, exclude

class Model(BaseModel):
    field1: bool = Field(strict=True)
    field2: bool 

m = Model(field1=True, field2=1)
print(m)

try:
    m = Model(field1=1, field2=True)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    model_config = ConfigDict(strict=True,validate_default=False)
    field1: bool = Field(strict=False)
    field2: bool = Field(default=1,validate_default=True)

try:
    m = Model(field1=1)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    f1: int = Field(frozen=True)
    f2: int = 5

m = Model(f1=3,f2=5)
print(m)
try:
    m.f1=20  # error: field is frozen / instance is frozen.
except ValidationError as ex:
    print(ex)


# exclude field from serialization

class Model(BaseModel):
    f1: int = Field(exclude=True)
    f2: int = 5
    f3: int = 6

m = Model(f1=3)
print(m.model_dump())
print(m.model_dump(include=['f1','f2']))  # this will not override.



