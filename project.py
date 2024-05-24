from pydantic import BaseModel,ValidationError
from datetime import date

class Automobile(BaseModel):
    manufacturer: str
    series_name: str
    type: str
    is_electric: bool = False
    manufactured_date: date
    base_msrp_usd: float
    vin: str
    number_of_doors: int = 4
    registration_company: str | None = None
    license_plate: str | None = None
