
from country_data import countries

valid_countries = [x for x in countries]
lookup_country_code = {name:code for name,code in countries.values()}


def lookup_country(name: str) -> tuple[str,str]:
    try:
        return countries[name]
    except KeyError:
        raise ValueError("Unknown country. "
                         f"Country name must be one of {",".join(valid_countries)}"
                        )
    
    
def date_serializer(value):
    value = value.strftime("%Y/%m/%d")
    return value