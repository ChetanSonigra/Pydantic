from pydantic import BaseModel,ValidationError, ConfigDict, Field,field_serializer
from pydantic.alias_generators import to_camel
from datetime import date
from enum import Enum

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

    manufacturer: str
    series_name: str
    type_: AutomobileType = Field(alias="type")
    is_electric: bool = False
    manufactured_date: date = Field(validation_alias="completionDate")
    base_msrp_usd: float = Field(validation_alias="msrpUSD",serialization_alias="baseMSRPUSD")
    vin: str
    number_of_doors: int = Field(validation_alias="doors",default=4)
    registration_country: str | None = None
    license_plate: str | None = None

    @field_serializer("manufactured_date",when_used='json-unless-none',)
    def manufactured_date_serializer(self,value):
        value = value.strftime("%Y/%m/%d")
        return value


data_json = '''
{
    "manufacturer": "BMW",
    "seriesName": "M4",
    "type": "Convertible",
    "isElectric": false,
    "completionDate": "2023-01-01",
    "msrpUSD": 93300,
    "vin": "1234567890",
    "doors": 2,
    "registrationCountry": "France",
    "licensePlate": "AAA-BBB"
}
'''


m = Automobile.model_validate_json(data_json)

print(m.model_dump())
print(m.model_dump(by_alias=True))
print(m.model_dump_json())
print(m.model_dump_json(by_alias=True))