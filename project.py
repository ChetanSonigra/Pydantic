from pydantic import BaseModel,ValidationError, ConfigDict
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
                              validate_assignment=True)

    manufacturer: str
    series_name: str
    type_: AutomobileType
    is_electric: bool = False
    manufactured_date: date
    base_msrp_usd: float
    vin: str
    number_of_doors: int = 4
    registration_company: str | None = None
    license_plate: str | None = None
