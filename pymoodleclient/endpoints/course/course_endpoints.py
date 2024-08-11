from dataclasses import dataclass as __dataclass
from pymoodleclient.endpoints.base import Endpoint
from .course_responses import CourseList
from requests import get


@__dataclass
class GetAllCourses(Endpoint):
    """Get all courses from moodle.
    Courses appears in `Course` class"""

    response_object = CourseList
    request_type = get
    function_name = "core_course_get_courses"
