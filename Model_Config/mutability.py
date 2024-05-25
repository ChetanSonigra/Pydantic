from pydantic import BaseModel,ConfigDict,ValidationError

class Model(BaseModel):
    field: int

m = Model(field=10)
m.field=20
print(m)

try:
    d = {m: 'This does not work!'}
except TypeError as ex:
    print(ex)




class Model(BaseModel):
    model_config = ConfigDict(frozen=True)
    field: int

m = Model(field=10)
try:
    m.field=20
except ValidationError as ex:
    print(ex)
 
try:
    d = {m: 'This works!'}
    print(d)
except TypeError as ex:
    print(ex)
