from pydantic import BaseModel,ValidationError

class Circle(BaseModel):
    center: tuple[int, int] = (0, 0)
    radius: int


print(Circle(radius=1))
print(Circle(center=(1, 1), radius=2))

class Circle(BaseModel):
    center: tuple[int, int] = "sf"  # this is not validated similar to when we assign value to attribute.
    radius: int


print(Circle(radius=1))

# Default in pydantic is different than python/dataclasses. means it will be same for all the instances.


# Nullable fields:
from typing import Union,Optional

# below 3 options serves the same purpose of allowing null/None as value and they are optional with default vlaue as None.
class Model(BaseModel):
    field_1: int | None
    field_2: Union[int, None]
    field_3: Optional[int]

try: 
    print(Model.__fields__)
    m = Model(field_1=None,field_2=None,field_3=None)
    m = Model()
except ValidationError as ex:
    print(ex)
