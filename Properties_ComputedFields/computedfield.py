from functools import cached_property
from pydantic import BaseModel, Field, ValidationError, computed_field, PydanticUserError
from math import pi


try:
    class Circle(BaseModel):
        center: tuple[int, int] = (0, 0)
        radius: int = Field(default=1, gt=0, frozen=True)
    
        @computed_field(alias='AREA', repr=False)
        @property
        def area(self) -> float:
            print("calculating area...")
            return pi * self.radius ** 2    
        
except PydanticUserError as ex:
    print(ex)

c = Circle()
print(c)  # calculates area here.
print(c.model_dump())
print(c.model_dump_json())
print(c.model_dump(by_alias=True))


class Circle(BaseModel):
    center: tuple[int, int] = (0, 0)
    radius: int = Field(default=1, gt=0, frozen=True)

    @computed_field(alias='AREA', repr=False)
    @cached_property
    def area(self) -> float:
        print("calculating area...")
        return pi * self.radius ** 2    
    

c = Circle()
print(c)
print(c.area)
print(c.area)