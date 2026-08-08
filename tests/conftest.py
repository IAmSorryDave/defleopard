import pytest
from dataclasses import dataclass


@pytest.fixture
def my_test_function():
    def my_function(*args, c=2, d="baz", z=False, **kwargs):
        return locals().copy()
    return my_function


@pytest.fixture
def my_test_class():
    

class MyClass:
    z = True

    def my_bare_method(*args, c=2, d="baz", z=False, **kwargs):
        return my_function(*args, c=c, d=d, z=z, **kwargs)

    my_class_method = classmethod(my_function)

    my_method = my_function

    my_static_method = staticmethod(my_function)

    my_property = property(my_function)


class MySubClass(MyClass):
    d = "qux"


@dataclass
class MyDataClass:
    c: int = 3
    d: str = "baz"
    z: bool = True

    my_method = my_function

    my_property = property(my_function)

@pytest.fixture
def project_directory_path():
    from pathlib import Path

    return Path(__file__).parent.parent


@pytest.fixture
def project_configuration(project_directory_path):
    from tomllib import load

    with open(project_directory_path / "pyproject.toml", "rb") as f:
        configuration = load(f)
    return configuration


@pytest.fixture
def project_metadata(project_configuration):
    return project_configuration.get("project")


@pytest.fixture
def project_name(project_metadata):
    return project_metadata.get("name")
