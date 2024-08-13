# pymoodleclient
[![PyPI version](https://badge.fury.io/py/pymoodleclient.svg)](https://badge.fury.io/py/pymoodleclient)

Pymoodleclient package provides simple
and powerfull client for Moodle webservices.

## Installation
To install pymoodleclient package you just type
```shell
pip install pymoodleclient
```
or
```shell
poetry add pymoodleclient
```

## Usage
To use package, you need to import `Client` class and `endpoints` module
```python
from pymoodleclient import Client, endpoints

client = Client("moodle_url", "api_token")
course_list = client.call(endpoints.course.GetAllCourses)
```
