from dataclasses import dataclass as __dataclass
from pymoodleclient.endpoints.base import Endpoint, QueryParams
from .cohort_responses import CohortList
from requests import get


a = Quer


@__dataclass
class GetCohort(Endpoint):
    """Return cohort with specified `cohortids`.
    If cohortids is`None`, returns all cohorts"""

    response_object = CohortList
    request_type = get
    function_name = "core_cohort_get_cohorts"
    # query_params = ''
