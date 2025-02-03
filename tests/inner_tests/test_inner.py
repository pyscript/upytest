"""
Some tests in a submodule. Ensures the inner conftest is used / read.
"""

def test_passes():
    """
    A test function that passes with a true assertion.
    """
    assert True, "This test passes"


def test_fails():
    """
    A test function that fails with a false assertion.
    """
    assert False, "This test will fail"