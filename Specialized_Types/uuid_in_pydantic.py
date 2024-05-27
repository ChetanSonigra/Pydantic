from uuid import uuid4
from pydantic import BaseModel,ValidationError,UUID4, Field

print(uuid4())

class Person(BaseModel):
    id: UUID4

p = Person(id=uuid4())
print(p)
print(p.model_dump())
print(p.model_dump_json())

class Person(BaseModel):
    id: UUID4 = uuid4()

p1 = Person()
p2 = Person()
print(p1.id, p2.id) 
# both are same because default is calculated once only.

# To run function for every instance created, use default_factory.

class Person(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)

p1 = Person()
p2 = Person()
print(p1.id, p2.id)