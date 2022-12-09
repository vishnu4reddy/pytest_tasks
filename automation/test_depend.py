# import pytest
# @pytest.mark.dependency()
# @pytest.mark.xfail(reason="deliberate fail")
# def test_a():
#     pass
#     assert True
# @pytest.mark.dependency()
# def test_b():
#     pass
# @pytest.mark.dependency(depends=["test_a"])
# def test_c():
#     pass
# @pytest.mark.dependency(depends=["test_b"])
# def test_d():
#     pass
# @pytest.mark.dependency(depends=["test_b", "test_c"])
# def test_e():
#     pass
import pytest
@pytest.mark.dependency(name="a")
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False
@pytest.mark.dependency(name="b")
def test_b():
    pass
@pytest.mark.dependency(name="c", depends=["a"])
def test_c():
     pass
@pytest.mark.dependency(name="d", depends=["b"])
def test_d():
    pass
@pytest.mark.dependency(name="e", depends=["b", "c"])
def test_e():
   pass