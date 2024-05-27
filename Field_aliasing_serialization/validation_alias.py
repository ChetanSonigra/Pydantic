from pydantic import BaseModel,ConfigDict, ValidationError, Field, AliasChoices
from pydantic.alias_generators import to_camel

class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_name: str = Field(validation_alias='FirstName')

m = Model(FirstName='Chetan')
print(m)
print(m.model_dump(), m.model_dump(by_alias=True))


class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_name: str = Field(validation_alias='FirstName',alias='firstName')
 
m = Model(FirstName='Chetan')   # does not work with firstName.
print(m)
print(m.model_dump(), m.model_dump(by_alias=True))


class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_name: str = Field(validation_alias='FirstName',
                            alias='firstName',
                            serialization_alias='givenName')

m = Model(FirstName='Chetan')
print(m)
print(m.model_dump(), m.model_dump(by_alias=True))


class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    
    first_name: str = Field(
        validation_alias=AliasChoices("FirstName", "GivenName"), 
        serialization_alias="givenName"
    )
    last_name: str

data = {
    "FirstName": "Chetan",
    "lastName": "Sonigra"
}
m = Model.model_validate(data)
print(m)
print(m.model_dump(by_alias=True))

data = {
    'GivenName': 'Chetan',
    'lastName': 'Sonigra'
}
m = Model.model_validate(data)
print(m)
print(m.model_dump(by_alias=True))

data = {
    'GivenName': 'Chetan',
    'FirstName': 'Chetan2',   # Last one will be used if many validation alias available in data.
    'lastName': 'Sonigra'
}
m = Model.model_validate(data)
print(m)
print(m.model_dump(by_alias=True))

# Use Case of AliasChoices: setting file to connect with various database.

data = {
    "databases": {
        "redis": {
            "name": "Local Redis",
            "redis_conn": "redis://secret@localhost:9000/1"
        },
        "pgsql": {
            "name": "Local Postgres",
            "pgsql_conn": "postgresql://user:secret@localhost"
        },
        "nosql": {
            "name": "Local MongoDB",
            "mongo_conn": "mongodb://USERNAME:PASSWORD@HOST/DATABASE"
        }
    }
}

class Database(BaseModel):
    name: str
    connection: str = Field(
        validation_alias=AliasChoices("redis_conn", "pgsql_conn", "mongo_conn")
    )

class Databases(BaseModel):
    databases: dict[str,Database]

databases = Databases.model_validate(data)
print(databases)
print(databases.model_dump_json(indent=2))



