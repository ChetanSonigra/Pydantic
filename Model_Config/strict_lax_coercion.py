from pydantic import BaseModel, ValidationError, Field, ConfigDict

class Model(BaseModel):
    field_1: str  #= Field(strict=True) - to make specific field strict.
    field_2: float 
    field_3: list
    field_4: tuple

try:
    m = Model(field_1=100, field_2=1, field_3=(1, 2, 3), field_4=[1, 2, 3])
    print(m)
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    model_config = ConfigDict(strict=True)
    field_1: str 
    field_2: float
    field_3: list
    field_4: tuple

    # class Config:
    #     strict = True
    #     # strict_types = True

try:
    m = Model(field_1=100, field_2=1, field_3=(1, 2, 3), field_4=[1, 2, 3])
    print(m)
except ValidationError as ex:
    print(ex)



json_data = '''
{
    "field_1": true,
    "field_2": 10.5,
    "field_3": 10,
    "field_4": null,
    "field_5": [1, 2, 3],
    "field_6": {
        "a": 1,
        "b": 2,
        "c": [3, 4, 5]
    },
    "field_7": [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
}
'''


import json
from pprint import pprint

data = json.loads(json_data)
pprint(data)


# Using pydantic model to convert json data into required python data type.

json_data = '''
{
    "field_1": true,
    "field_2": 10,
    "field_3": 1,
    "field_4": null,
    "field_5": [1, 2, 3],
    "field_6": ["a", "b", "c"],
    "field_7": {"a": 1, "b": 2}
}
'''

class Model(BaseModel):
    field_1: bool
    field_2: float
    field_3: int
    field_4: str | None
    field_5: tuple[int, ...]
    field_6: set[str]
    field_7: dict

m = Model.model_validate_json(json_data, strict= True)
print(m)

