from pydantic import ValidationError, BaseModel, ConfigDict, Field, PositiveInt
# lt,le, gt, ge, multiple_of

class Model(BaseModel):
    id: int = Field(gt=0) # same as PositiveInt

print(Model.model_fields)

class Model(BaseModel):
    id: PositiveInt

print(Model.model_fields)

class Model(BaseModel):
    id: float = Field(gt=2,lt=10, multiple_of=2)

m = Model(id=4)
print(m)

try:
    m = Model(id=3) # 3,5,7,9, <= 2, >=10  won't work
except ValidationError as ex:
    print(ex)

