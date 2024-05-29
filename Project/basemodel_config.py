from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelBaseModel(BaseModel):
    model_config = ConfigDict(extra='forbid',
                            str_strip_whitespace=True,
                            validate_default=True,
                            validate_assignment=True,
                            alias_generator=to_camel)