import pytest

from package.app import SomeExampleApp


@pytest.fixture
def instance():
    return SomeExampleApp('test')


def test_calls_count(instance):
    assert instance.ncalls == 0
    assert instance.name == 'test'

    assert instance.power(2, 3) == 8
    assert instance.ncalls == 1
