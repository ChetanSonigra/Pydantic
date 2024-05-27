from typing import Annotated, get_args

SpecialInt = Annotated[int, "metadata", [1,2,3],100]

print(get_args(SpecialInt))

from pydantic import BaseModel, Field,  ValidationError

class Model(BaseModel):
    x: int = Field(gt=0,le=100)
    y: int = Field(gt=0,le=100)
    z: int = Field(gt=0,le=100)

print(Model.model_fields)

BoundedInt = Annotated[int,Field(gt=0,le=100)]

class Model(BaseModel):
    x: BoundedInt
    y: BoundedInt
    z: BoundedInt

print(Model.model_fields)
print(Model(x=1,y=3,z=10))

try:
    Model(x=0,y=4,z=103)
except ValidationError as ex:
    print(ex)