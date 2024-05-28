from pydantic import BaseModel, Field, ValidationError
from math import pi
from functools import cached_property


class MyCircle(BaseModel):
    center: tuple[int,int] = (0,0)
    radius: float = Field(default=1,gt=0)

    def area(self):
        return pi*self.radius**2
    
c = MyCircle()
print(c)
print(c.area())
print(c.model_dump())


# property
class MyCircle(BaseModel):
    center: tuple[int,int] = (0,0)
    radius: float = Field(default=1,gt=0)

    @property
    def area(self):
        return pi*self.radius**2
    
c = MyCircle()
print(c)
print(c.area)
print(c.model_dump())


# cachedproperty
class MyCircle(BaseModel):
    center: tuple[int,int] = (0,0)
    radius: float = Field(default=1,gt=0,frozen=True)

    @cached_property
    def area(self):
        print('calculating area...')
        return pi*self.radius**2
    
c = MyCircle()
print(c)
print(c.area)
print(c.area)
print(c.model_dump())
print(c.model_fields)

try:
    c.radius = 20
except ValidationError as ex:
    print(ex)