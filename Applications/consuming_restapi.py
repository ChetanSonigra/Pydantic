import requests
from pydantic import BaseModel, Field, field_validator, ValidationError, IPvAnyAddress, ConfigDict


class IPGeo(BaseModel):
    model_config = ConfigDict(extra='ignore')

    ip: IPvAnyAddress
    country: str | None = None
    country_code: str | None = Field(default=None, min_length=2, max_length=2)
    country_code3: str | None = Field(default=None, min_length=3, max_length=3)
    city: str | None = None
    region: str | None = None
    timezone: str | None = None
    organization_name: str | None = None

    @field_validator('organization_name', mode='after')
    @classmethod
    def set_unknown_to_none(cls,value):
        if value == "Unknown".casefold():
            value = None
        return None
    

ipgeo  =  IPGeo(ip='8.8.8.8',country='test', country_code='US',country_code3='USA', organization_name='Unknown')

url_query = "https://get.geojs.io/v1/geo/{ip_address}.json"

url =url_query.format(ip_address='8.8.8.8')
response = requests.get(url)
response.raise_for_status()
response_json = response.json()
print(response_json)

data = IPGeo.model_validate(response_json)
print(data)
print(data.model_dump_json(indent=2))


url = "https://get.geojs.io/v1/ip.json"
response = requests.get(url)
response.raise_for_status()
response_json = response.json()
data = IPGeo.model_validate(response_json)
print(data.model_dump_json(indent=2))
