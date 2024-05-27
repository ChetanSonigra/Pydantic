from pydantic import BaseModel,PositiveInt,ValidationError

class Circle(BaseModel):
    center: tuple[int,int] = (0,0)
    radius: PositiveInt = 1

c = Circle(center=(1,2))
print(c)

try: 
    Circle(center=(0.5,0.5),radius=-1)
except ValidationError as ex:
    print(ex)

print(Circle.model_fields)