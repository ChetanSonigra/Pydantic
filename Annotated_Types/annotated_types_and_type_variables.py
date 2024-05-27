from pydantic import BaseModel, ConfigDict, Field, ValidationError

from typing import Annotated, TypeVar, Any

BoundedListInt = Annotated[list[int],Field(max_length=5)]

class Model(BaseModel):
    f1: BoundedListInt = []
    f2: BoundedListInt = []

m = Model()
print(m)

# similarly,
BoundedListFloat = Annotated[list[float],Field(max_length=5)]
BoundedListString = Annotated[list[str], Field(max_length=5)]
# or
BoundedListAny = Annotated[list[Any], Field(max_length=5)]

# instead of separate, we can do 
T = TypeVar('T')
BoundedList = Annotated[list[T],Field(max_length=5)]

class Model(BaseModel):
    integers: BoundedList[int]
    strings: BoundedList[str]

m = Model(integers=[1,2,4],strings=['a','b'])
print(m)

try:
    Model(integers=[x for x in range(6)],strings=[x for x in range(5)])
except ValidationError as ex:
    print(ex)
