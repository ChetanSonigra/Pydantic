from pydantic import BaseModel, ConfigDict, ValidationError, Field
# sequence constraint: min_length, max_length

class Model(BaseModel):
    name: str = Field(min_length=2, max_length=10)

m = Model(name='Chetan')
print(m)

try:
    m = Model(name='a'*11)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    items: list[int] = Field(min_length=2, max_length=5,default=[0,0,0])

m = Model(items=[1,2,3])
print(m)

try:
    m = Model(items=[1])
except ValidationError as ex:
    print(ex)


#  tuple[int] doesn't work like list[int].
# Have to use tuple[int,...] for allowing multiple values.

class Model(BaseModel):
    items: tuple[int,...] = Field(min_length=2,max_length=3,default=(1,2,3))

try:
    m = Model(items=(1,2,3,4))
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    zip_code: str = Field(pattern=r"^[0-9]{5}(?:-[0-9]{4})?$")

m = Model(zip_code="12345-1234")
print(m)

try:
    Model(zip_code='12345-12345')
except ValidationError as ex:
    print(ex)

