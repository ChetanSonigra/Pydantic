from pydantic import BaseModel, ConfigDict, ValidationError,Field

class Model(BaseModel):
    field: str

m1= Model(field='   python   ')
m2 = Model(field='   python \t \n')

print(m1,m2,sep='\n')
print(m1==m2)

class Model(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True,str_to_upper=True)
    field: str

m1= Model(field='   python   ')
m2 = Model(field='   python \t \n')

print(m1,m2,sep='\n')
print(m1==m2)