from dataclasses import dataclass as __dataclass, field
from .endpoints.base import Endpoint


@__dataclass
class Params:
    wstoken: str
    wsfunction: Endpoint
    moodlewsrestformat: str = field(default="json")
