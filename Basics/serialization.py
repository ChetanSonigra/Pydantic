from pydantic import BaseModel,ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


p = Person(first_name='Chetan', last_name='Sonigra', age=25)
p2 = Person(first_name='Ram', last_name='Sonigra', age=26)

print(p.__dict__)
print(p.model_dump(), type(p.model_dump()))
print(p.model_dump_json(),type(p.model_dump_json()))

print(p.model_dump_json(indent=2, exclude={'age'}))

print(p.model_dump(include={'first_name','age'}))

