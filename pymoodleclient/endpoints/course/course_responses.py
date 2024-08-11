from dataclasses import dataclass as __dataclass, InitVar
from typing import Optional

from pymoodleclient.endpoints.base import ResponseObject


@__dataclass
class CourseFormatOption:
    name: str
    value: int


@__dataclass
class Course:
    id: int
    shortname: str
    categoryid: int
    categorysortorder: str
    fullname: str
    displayname: str
    idnumber: int
    summary: str
    summaryformat: int
    format: str
    showgrades: int
    newsitems: int
    startdate: int
    enddate: int
    numsections: int
    maxbytes: int
    showreports: int
    visible: int
    groupmode: int
    groupmodeforce: int
    defaultgroupingid: int
    timecreated: int
    timemodified: int
    enablecompletion: int
    completionnotify: int
    lang: int
    forcetheme: int
    courseformatoptions: list[CourseFormatOption]

    def __post_init__(self):
        self.courseformatoptions = [
            CourseFormatOption(**course_format_option)
            for course_format_option in self.courseformatoptions
        ]


@__dataclass
class CourseList(ResponseObject):
    courses: list[Course]

    def __post_init__(self):
        for course in self.courses:
            if "hiddensections" in course.keys():
                course.pop("hiddensections")
            self.courses[self.courses.index(course)] = Course(**course)
