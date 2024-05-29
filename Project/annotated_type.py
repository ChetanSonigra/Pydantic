from typing import TypeVar, Annotated
from pydantic import Field, AfterValidator, PlainSerializer
from datetime import date
from helper_functions import date_serializer, lookup_country

T = TypeVar('T')
BoundedString = Annotated[str,Field(min_length=2, max_length=50)]
BoundedList = Annotated[list[T],Field(min_length=1, max_length=5)]
Country = Annotated[BoundedString,AfterValidator(lambda name:lookup_country(name)[0])]
CustomDate = Annotated[date,PlainSerializer(date_serializer,when_used='json-unless-none')]
