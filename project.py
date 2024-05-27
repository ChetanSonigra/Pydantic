from pydantic import BaseModel,ValidationError, ConfigDict, Field,field_serializer, UUID4
from pydantic.alias_generators import to_camel
from datetime import date
from uuid import uuid4
from enum import Enum
from typing import Annotated, TypeVar


T = TypeVar('T')
BoundedString = Annotated[str,Field(min_length=2, max_length=50)]
BoundedList = Annotated[list[T],Field(min_length=1, max_length=5)]


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
    registration_country: BoundedString | None = None
    license_plate: BoundedString | None = None

    @field_serializer("manufactured_date",when_used='json-unless-none',)
    def manufactured_date_serializer(self,value):
        value = value.strftime("%Y/%m/%d")
        return value

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
    "registrationCountry": "France",
    "licensePlate": "AAA-BBB"
}


m = Automobile.model_validate(data)

print(m.model_dump())
print(m.model_dump(by_alias=True))
print(m.model_dump_json())
print(m.model_dump_json(by_alias=True))