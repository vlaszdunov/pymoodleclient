from dataclasses import dataclass as __dataclass, InitVar
from typing import Optional

from pymoodleclient.endpoints.base import ResponseObject


@__dataclass
class CohortList:
    name: str
    value: int
