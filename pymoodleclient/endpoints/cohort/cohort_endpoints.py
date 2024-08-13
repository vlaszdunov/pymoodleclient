from dataclasses import dataclass as __dataclass, field, InitVar
from pymoodleclient.endpoints.base import Endpoint, QueryParams
from .cohort_responses import CohortList
from requests import get
from typing import Optional, Callable


@__dataclass
class GetCohortParams(QueryParams):
    list_of_cohortids: InitVar[list[int]]

    def __post_init__(self, list_of_cohortids: list[int]):
        for i in range(len(list_of_cohortids)):
            setattr(self, f"cohortids[{i}]", list_of_cohortids[i])


@__dataclass
class GetCohort(Endpoint):
    """Return cohort with specified `cohortids`.
    If cohortids is `None`, returns all cohorts"""

    query_params: Optional[GetCohortParams]
    function_name: str = field(default="core_cohort_get_cohorts")
    response_object: CohortList = field(default=CohortList)
    request_type: Callable = field(default=get)

    def __post_init__(self):
        if hasattr(self, "query_params"):
            self.query_params = GetCohortParams(self.query_params)
