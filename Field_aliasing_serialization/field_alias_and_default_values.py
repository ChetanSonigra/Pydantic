# when deserializing - validation alias/alias
# name in pydantic - field name
# name when serializing - serialization alias/fieldname/alias

from pydantic import BaseModel,ConfigDict, ValidationError,Field

class Model(BaseModel):
    id_: int = Field(alias='id',default=100)
    first_name: str = Field(alias='firstName')

json_data = """
{
    "id": 1,
    "firstName": "Chetan"
}
"""
m = Model.model_validate_json(json_data)
print(m)
print(Model(id=2,firstName='Ram'))  
try:
    Model(id_=3,first_name='sdkfj')     # can only use alias name while creating Model.
except ValidationError as ex:
    print(ex)

print(m.model_dump())
print(m.model_dump(by_alias=True)) # To serialize based on alias.
print(m.model_dump_json(by_alias=True))
print(m.model_fields)

print(Model(firstName='Chetan'))   # Using default values using 