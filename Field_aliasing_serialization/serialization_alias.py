from pydantic import BaseModel,ConfigDict,ValidationError,Field

response_json = """
{
    "ID": 100,
    "FirstName": "Chetan",
    "lastname": "Sonigra"
}
"""

class Person(BaseModel):
    id_: int = Field(alias='ID',serialization_alias='id')
    first_name: str = Field(alias='FirstName',serialization_alias='firstName')
    last_name: str = Field(alias='lastname',serialization_alias='lastName')

p = Person.model_validate_json(response_json)
print(p)
print(p.model_dump())
print(p.model_dump(by_alias=True))
print(p.model_fields)