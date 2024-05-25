from pydantic import BaseModel, ValidationError


class Coordinates(BaseModel):
    x: float
    y: float


p1 = Coordinates(x=1.1, y=2.2)
print(p1)

p1 = Coordinates(x=0, y="2.2")
print(p1)

data ={"x": 0, "y": "2.2"}
p1 = Coordinates.model_validate(data)
print(p1)

# to know more, check pydantic doc about lax and strict mode.