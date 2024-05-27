from pydantic import BaseModel,ValidationError, conlist, PositiveInt

class Circle(BaseModel):
    center: tuple[int,int] = (0,0)
    radius: PositiveInt = 1

class Sphere(BaseModel):
    center: tuple[int,int] | tuple[int,int,int] = (0,0)
    radius: PositiveInt = 1

try:
    Sphere(center=(0,0,0,0))
except ValidationError as ex:
    print(ex)          
# validation message not clear.


class Sphere(BaseModel):
    center: conlist(int,min_length=2,max_length=3) = [0,0] # type: ignore
    radius: PositiveInt = 1

try:
    s = Sphere(center=(0,0,0))  # tuple of length less than 2 and more than 3 will throw an error.
    print(s)
except ValidationError as ex:
    print(ex)      

