from pydantic import BaseModel, ValidationError, ConfigDict, EmailStr,NameEmail,AnyUrl, HttpUrl
# To use this, need to install email-validator module.

class Model(BaseModel):
    email: EmailStr

m = Model(email='abcd.sjf@gmail.com')
print(m)
print(type(m.email))

try:
    m = Model(email="fkj.kj@gmail")
except ValidationError as ex:
    print(ex)


class Model(BaseModel):
    email: NameEmail

m = Model(email="abcd.sjf@gmail.com")
print(m.email.email, type(m.email.email))
print(m.email.name,type(m.email.name))

m = Model(email="Abcd Sjf <abcd.sjf@gmail.com>")
print(m.email.email)
print(m.email.name)
print(m.model_dump())
print(m.model_dump_json())

url = AnyUrl("https://www.google.com/search?q=pydantic")
print(url.scheme)
print(url.host)
print(url.path)
print(url.query)
print(url.port)
print(url.username)
print(url.password)

url = AnyUrl("ftp://user_name:user_password@ftp.myserver.com:21")
print(url.scheme)
print(url.host)
print(url.path)
print(url.query)
print(url.port)
print(url.username)
print(url.password)

# Url is more broad. HttpUrl is specifically used for http/https url.

class ExternalAPI(BaseModel):
    root_url: HttpUrl

m = ExternalAPI(root_url="https://api.myserver.com")
print(m)

from pydantic import IPvAnyAddress

class Model(BaseModel):
    ip: IPvAnyAddress

m = Model(ip="127.0.0.1")
print(m)
print(m.ip.exploded)
print(m.ip.version)
print(m.ip.is_loopback)

m = Model(ip="::1")
print(m)
print(m.ip.exploded)
print(m.ip.version)
print(m.ip.is_loopback)





