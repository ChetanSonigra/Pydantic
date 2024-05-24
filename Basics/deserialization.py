
# Deserialization is the act of taking data (that can be provided in a number of ways)
# to create and populate a new model instance.

from pydantic import BaseModel,ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


data = {
    'first_name': 'Chetan',
    'last_name': 'Sonigra',
    'age': 24
}

# 1: 
p = Person(**data)
# 2: 
p = Person.parse_obj(data)
print(p)

data_json = """
{
    "first_name": "Chetan",
    "last_name": "Sonigra",
    "age": 24
}
"""

p = Person.parse_raw(data_json)
print(p)