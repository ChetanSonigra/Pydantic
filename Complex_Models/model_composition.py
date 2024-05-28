from pydantic import ConfigDict, Field, ValidationError, BaseModel, \
    EmailStr, PastDate, AfterValidator
from pydantic.alias_generators import to_camel
from typing import Annotated

class Point2D(BaseModel):
    x: float = 0
    y: float = 0

class Circle(BaseModel):
    center: Point2D
    radius: float = Field(default=1, gt=0)

try:
    c = Circle(center=(1,1))
except ValidationError as ex:
    print(ex)

try:
    c = Circle(center={"x":1,"y":1})
    print(c)
except ValidationError as ex:
    print(ex)

c = Circle(center=Point2D(x=1,y=1),radius=4)
print(c)
print(c.model_dump())
print(c.model_dump_json())
print(c.center, c.center.x)
# deserialization using dict or json going to result into same.


json_data = """
{
    "firstName": "David",
    "lastName": "Hilbert",
    "contactInfo": {
        "email": "d.hilbert@spectral-theory.com",
        "homePhone": {
            "countryCode": 49,
            "areaCode": 551,
            "localPhoneNumber": 123456789
        }
    },
    "personalInfo": {
        "nationality": "German",
        "born": {
            "date": "1862-01-23",
            "place": {
                "city": "Konigsberg",
                "country": "Prussia"
            }
        },
        "died": {
            "date": "1943-02-14",
            "place": {
                "city": "Gottingen",
                "country": "Germany"
            }
        }
    },
    "awards": ["Lobachevsky Prize", "Bolyai Prize", "ForMemRS"],
    "notableStudents": ["von Neumann", "Weyl", "Courant", "Zermelo"]
}
"""


class ContactInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')

    email: EmailStr | None = None

class PlaceInfo(BaseModel):
    city: str
    country: str

class PlaceDateInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    date_: PastDate = Field(alias='date')
    place: PlaceInfo

class PersonalInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')

    nationality: str
    born: PlaceDateInfo

class Person(BaseModel):
    model_config =ConfigDict(alias_generator=to_camel, populate_by_name=True, extra='ignore')

    first_name: str
    last_name: str
    contact_info: ContactInfo = Field(repr=False)
    personal_info: PersonalInfo = Field(repr=False)
    notable_students: list[str] = Field(default=[],repr=False)

p = Person.model_validate_json(json_data)
print(p)
print(p.model_dump_json(by_alias=True, indent=2))


SortedStringList = Annotated[list[str], AfterValidator(lambda value: sorted(value,key=str.casefold))]
class Person(BaseModel):
    model_config =ConfigDict(alias_generator=to_camel, populate_by_name=True, extra='ignore')

    first_name: str
    last_name: str
    contact_info: ContactInfo = Field(repr=False)
    personal_info: PersonalInfo = Field(repr=False)
    notable_students: SortedStringList = Field(default=[],repr=False)

p = Person.model_validate_json(json_data)
print(p)
print(p.model_dump_json(by_alias=True, indent=2))