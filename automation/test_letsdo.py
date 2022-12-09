import pytest
@pytest.fixture(scope="class")
def class_test():
    assert ("scope class")


def test_class2(class_test):
    assert ("scope class2")