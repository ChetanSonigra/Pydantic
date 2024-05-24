from pydantic import BaseModel,ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


p = Person(first_name='Chetan', last_name='Sonigra', age=25)
p2 = Person(first_name='Ram', last_name='Sonigra', age=26)

print(p.__dict__)
print(p.dict(), type(p.dict()))
print(p.json(),type(p.json()))

print(p.json(indent=2, exclude={'age'}))

print(p.dict(include={'first_name','age'}))

