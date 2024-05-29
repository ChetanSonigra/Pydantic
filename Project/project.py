from pydantic import ValidationError, Field, UUID4, field_validator, \
                        ValidationInfo, computed_field
from pydantic.alias_generators import to_camel
from datetime import date
from uuid import uuid4
from functools import cached_property
from helper_functions import lookup_country_code
from annotated_type import Country, BoundedString, BoundedList, CustomDate
from basemodel_config import CamelBaseModel
from enum_types import AutomobileType


class RegistrationCountry(CamelBaseModel):
    name: Country | None = Field(default=None)
    @computed_field
    @cached_property
    def code3(self) -> str:
        return lookup_country_code[self.name]


class Automobile(CamelBaseModel):
    
    id_: UUID4 = Field(alias='id',default_factory=uuid4)
    manufacturer: BoundedString 
    series_name: BoundedString 
    type_: AutomobileType = Field(alias="type")
    is_electric: bool = Field(default=False, repr=False)
    manufactured_date: CustomDate = Field(validation_alias="completionDate", ge=date(1980,1,1),repr=False)
    base_msrp_usd: float = Field(validation_alias="msrpUSD",serialization_alias="baseMSRPUSD",repr=False)
    top_features: BoundedList[BoundedString] | None = Field(default=None, repr=False)
    vin: BoundedString = Field(repr=False)
    number_of_doors: int = Field(validation_alias="doors",default=4,ge=2,le=4,multiple_of=2,repr=False)
    registration_country: RegistrationCountry | None = Field(default=None, repr=False)
    registration_date: CustomDate | None = Field(default=None, repr=False)
    license_plate: BoundedString | None = Field(default=None, repr=False)

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
    "registrationCountry": {"name": "us"},
    "registrationDate": "2023-06-01",
    "licensePlate": "AAA-BBB"
}


try:
    m = Automobile.model_validate(data)
    print(m)
    print(m.model_dump_json(by_alias=True,indent=2))
except ValidationError as ex:
    exception = ex.json(indent=2)



# print(m.model_dump())
# print(m.model_dump(by_alias=True))
# print(m.model_dump_json())

# print(m.registration_country_code)