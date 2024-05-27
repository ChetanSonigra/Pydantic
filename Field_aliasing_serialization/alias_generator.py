from pydantic import BaseModel,ConfigDict,ValidationError, Field
from pydantic.alias_generators import to_camel, to_pascal,to_snake

class Person(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)  # can use any custom function

    id_: int = Field(alias="id")
    first_name: str | None = None
    last_name: str
    age: int | None = None


p = Person(id=1,lastName='Sonigra')
print(p)
print(p.model_fields)
print(p.model_dump())
print(p.model_dump(by_alias=True))


# Deserialize by fieldname or alias

class Person(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel,populate_by_name=True)  # can use any custom function

    id_: int = Field(alias="id")
    first_name: str | None = None
    last_name: str
    age: int | None = None

p = Person(id=2,last_name='Sonigra') # can give field name or alias or both.
print(p.model_dump())
print(p)