from enum import Enum
from pydantic import BaseModel,ConfigDict,ValidationError

class Color(Enum):
    red = "Red"
    green = "Green"
    blue = "Blue"
    orange = "Orange"
    yellow = "Yellow"
    cyan = "Cyan"
    white = "White"
    black = "Black"


print(Color.red, Color.red.value)

class Model(BaseModel):
    color: Color

print(Model(color=Color.red))

data = """
{
    "color": "Red"
}
"""
m = Model.model_validate_json(data)
print(m)


data = """
{
    "color": "Magenta"
}
"""

try:
    Model.model_validate_json(data)
except ValidationError as ex:
    print(ex)


print(m.model_dump(), m.model_dump_json(), sep='\n')


class Model(BaseModel):
    model_config = ConfigDict(use_enum_values=True) 
    # this will not validate default value, so either use validate_default or use correct values in default.

    color: Color # = Color.red.value

m = Model(color=Color.cyan)

print(m.color, type(m.color))

