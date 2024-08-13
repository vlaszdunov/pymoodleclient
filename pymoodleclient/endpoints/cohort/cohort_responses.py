from dataclasses import dataclass as __dataclass
from typing import Optional

from pymoodleclient.endpoints.base import ResponseObject


@__dataclass
class Cohort:
    id: int
    name: str
    idnumber: str
    description: str
    descriptionformat: int
    visible: bool | int
    theme: str


@__dataclass
class CohortList(ResponseObject):
    cohorts_list: list[Cohort]

    def __post_init__(self):
        for i in range(len(self.cohorts_list)):
            self.cohorts_list[i] = Cohort(**self.cohorts_list[i])
