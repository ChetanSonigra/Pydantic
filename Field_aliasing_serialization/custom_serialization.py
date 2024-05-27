from pydantic import BaseModel, field_serializer, FieldSerializationInfo
from datetime import datetime

class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer('dt',when_used='always')
    def serialize_name(self,value):
        print(f'Type: {type(value)}')
        return value
    
m = Model(dt="2024-05-26T12:00:00")
print(m)
print(m.model_dump())
print(m.model_dump_json())
m = Model()
print(m)
print(m.model_dump())
print(m.model_dump_json())



class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer('dt',when_used='unless-none')
    def serialize_name(self,value,info: FieldSerializationInfo):
        print(f'Type: {type(value)}')
        print(info)
        print(info.mode_is_json())
        return value
    
m = Model(dt="2024-05-06T12:00:00")
print(m)
print(m.model_dump())
print(m.model_dump_json())
m = Model()
print(m)
print(m.model_dump())
print(m.model_dump_json())


class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer('dt',when_used='json-unless-none')
    def serialize_name(self,value,info: FieldSerializationInfo):
        print(info)                                  # printing serialization info.
        print(info.mode_is_json())
        return value.strftime("%Y/%m/%d %I:%M %p")   # format as required in case of json-unless-none.
    
m = Model(dt="2024-05-06T12:00:00")
print(m)
print(m.model_dump())
print(m.model_dump_json())
m = Model()
print(m)
print(m.model_dump())
print(m.model_dump_json())



# Use Case: 
import pytz

def make_utc(dt:datetime) -> datetime:
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt

print(make_utc(datetime.now()))
print(make_utc(datetime.now()).isoformat())

def dt_utc_json_serializer(dt:datetime) -> datetime:
    dt = make_utc(dt)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer("dt",when_used="unless-none")
    def dt_serializer(self,value,info: FieldSerializationInfo):
        if info.mode_is_json():
            return dt_utc_json_serializer(value)
        return make_utc(value)

m = Model(dt=datetime(2024,5,27))
print(m)
print(m.model_dump())
print(m.model_dump_json())

eastern = pytz.timezone('US/Eastern')
dt = eastern.localize(datetime(2024,5,27))

print(dt)
print(dt.astimezone(pytz.utc))
m = Model(dt=dt)
print(m)
print(m.model_dump())
print(m.model_dump_json())
