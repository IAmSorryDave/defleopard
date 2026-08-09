import pytest

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

from dataclasses import dataclass

@pytest.fixture
def my_dummy_function():
    def my_function(*args, c=2, d="baz", z=False, **kwargs):
        return locals().copy()
    return my_function


@pytest.fixture
def my_dummy_class(my_dummy_function):
    
    class MyClass:
        z = True
    
        def my_bare_method(*args, c=2, d="baz", z=False, **kwargs):
            return my_dummy_function(*args, c=c, d=d, z=z, **kwargs)
    
        my_class_method = classmethod(my_dummy_function)
    
        my_method = my_dummy_function
    
        my_static_method = staticmethod(my_dummy_function)
    
        my_property = property(my_dummy_function)

    return MyClass

@pytest.fixture
def my_dummy_subclass(my_dummy_class):
    
    class MySubClass(my_dummy_class):
        d = "qux"

    return MySubClass

@pytest.fixture
def my_dummy_dataclass(my_dummy_function):
    
    @dataclass
    class MyDataClass:
        c: int = 3
        d: str = "baz"
        z: bool = True
        
        my_method = my_dummy_function
        
        my_property = property(my_dummy_function)

    return MyDataClass
