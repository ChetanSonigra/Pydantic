from pydantic import BaseModel,ValidationError, ConfigDict, \
                        Field,field_serializer, UUID4, field_validator, ValidationInfo, AfterValidator
from pydantic.alias_generators import to_camel
from datetime import date
from uuid import uuid4
from enum import Enum
from typing import Annotated, TypeVar
from country_data import countries

T = TypeVar('T')
BoundedString = Annotated[str,Field(min_length=2, max_length=50)]
BoundedList = Annotated[list[T],Field(min_length=1, max_length=5)]
valid_countries = [x for x in countries]

def lookup_country(name: str) -> tuple[str,str]:
    try:
        return countries[name]
    except KeyError:
        raise ValueError("Unknown country. "
                         f"Country name must be one of {",".join(valid_countries)}"
                        )
        
Country = Annotated[BoundedString,AfterValidator(lambda name:lookup_country(name)[0])]

class AutomobileType(Enum):
    sedan = 'Sedan'
    coupe = 'Coupe'
    convertible = 'Convertible'
    suv = 'SUV'
    truck = 'Truck'


class Automobile(BaseModel):
    model_config = ConfigDict(extra='forbid',
                              str_strip_whitespace=True,
                              validate_default=True,
                              validate_assignment=True,
                              alias_generator=to_camel)
    
    id_: UUID4 = Field(alias='id',default_factory=uuid4)
    manufacturer: BoundedString
    series_name: BoundedString
    type_: AutomobileType = Field(alias="type")
    is_electric: bool = False
    manufactured_date: date = Field(validation_alias="completionDate", ge=date(1980,1,1))
    base_msrp_usd: float = Field(validation_alias="msrpUSD",serialization_alias="baseMSRPUSD")
    top_features: BoundedList[BoundedString] | None = None
    vin: BoundedString
    number_of_doors: int = Field(validation_alias="doors",default=4,ge=2,le=4,multiple_of=2)
    registration_country: Country | None = None
    registration_date: date | None = None
    license_plate: BoundedString | None = None

    @field_serializer("manufactured_date","registration_date",when_used='json-unless-none',)
    def manufactured_date_serializer(self,value):
        value = value.strftime("%Y/%m/%d")
        return value
    
    @field_validator('registration_date')
    @classmethod
    def registration_date_validator(cls,dt:date,info: ValidationInfo):
        data = info.data
        if 'manufactured_date' in data:
            if dt<data['manufactured_date']:
                raise ValueError("Registration date can not be prior to manufactured date.")
        return dt
    

data = {
    "id": "c4e60f4a-3c7f-4da5-9b3f-07aee50b23e7",
    "manufacturer": "BMW",
    "seriesName": "M4 Competition xDrive",
    "type": "Convertible",
    "isElectric": False,
    "completionDate": "2023-01-01",
    "msrpUSD": 93_300,
    "topFeatures": ["6 cylinders", "all-wheel drive", "convertible"],
    "vin": "1234567890",
    "doors": 2,
    "registrationCountry": "usa",
    "registrationDate": "2023-01-01",
    "licensePlate": "AAA-BBB"
}


try:
    m = Automobile.model_validate(data)
except ValidationError as ex:
    exception = ex.json(indent=2)


print(m)

# print(m.model_dump())
# print(m.model_dump(by_alias=True))
# print(m.model_dump_json())
print(m.model_dump_json(by_alias=True))