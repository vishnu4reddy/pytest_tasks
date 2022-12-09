import pytest
@pytest.fixture(scope="class")
def class_test():
    assert ("scope class")


def test_class2(class_test):
    assert ("scope class2")


# @pytest.fixture(scope="session")
# def session():
#     logging.info("scope session")
    
# @pytest.fixture(scope="package")
# def package():
#     logging.info("scope package"