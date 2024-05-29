from pydantic import Field, BaseModel, field_validator, ConfigDict, BeforeValidator
import csv
from typing import Annotated

with open('Applications/pop_estimates.csv') as f:
    data = csv.reader(f)
    for _ in range(5):
        print(next(data))


def name_int(value: str) -> int:
    try:
        return int(value.strip().replace(",",""))
    except Exception as ex:
        print(ex)

FunkyInt = Annotated[int, BeforeValidator(name_int)]

class Estimate(BaseModel):
    area: str
    july_1_2001: FunkyInt
    july_1_2000: FunkyInt
    april_1_2000: FunkyInt

with open('Applications/pop_estimates.csv') as f:
    data = csv.DictReader(f)
    for _ in range(5):
        print(next(data))

def estimates():
    with open('Applications/pop_estimates.csv') as f:
        data = csv.DictReader(f, fieldnames=['area','july_1_2001','july_1_2000','april_1_2000'])
        next(data)

        for row in data:
            yield Estimate.model_validate(row)

for estimate in estimates():
    print(estimate)


data = list(estimates())
