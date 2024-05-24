from pydantic import BaseModel,ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"

p = Person(first_name='Chetan', last_name='Sonigra', age=25)

print(p,p.age)
print(p.__fields__)
print(p.__fields_set__)     # to get set of fields provided by user/while creating instance.
print(p.display_name)
print(p.schema_json(by_alias=False)) # json schema generation.


try:
    Person(last_name='Sonigra')
except ValidationError as ex:
    print(ex)


# This throws error by default.
try: 
    Person(first_name='Chetan',last_name='Sonigra',age='twenty')
except ValidationError as ex:
    print(ex)

# This doesn't throw error by default.
p.age = 'Twenty'
print(p)