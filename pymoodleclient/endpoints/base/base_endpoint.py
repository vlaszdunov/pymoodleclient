from dataclasses import dataclass as __dataclass
from typing import Callable


@__dataclass
class QueryParams:
    "fegd"
    pass


@__dataclass
class Endpoint:
    """Base class of Endpoint Objects"""

    response_object: type
    request_type: Callable
    function_name: str
    query_params: QueryParams
