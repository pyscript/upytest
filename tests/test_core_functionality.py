"""
A test module that will just use global setup and teardown functions. (Check
the browser console for the output of the setup and teardown functions.)
"""

import upytest


@upytest.skip("This test will be skipped")
def test_skipped():
    """
    Test functions decorated with `@upytest.skip` will be skipped.
    """
    assert False  # This will not be executed.


@upytest.skip(
    "This test will be skipped with a skip_when condition", skip_when=True
)
def test_when_skipped():
    """
    Test functions decorated with `@upytest.skip` and a truthy when condition
    will be skipped.
    """
    assert False


@upytest.skip(
    "This test will NOT be skipped with a False-y skip_when",
    skip_when=False,
)
def test_when_not_skipped_passes():
    """
    Test functions decorated with `@upytest.skip` and a falsey when condition
    will NOT be skipped.
    """
    assert True, "This test passes"


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


def test_raises_expects_base_exception_children_passes():
    """
    Check that `upytest.raises` expects subclasses of `BaseException`. This
    test will pass.
    """
    # Must have expected exception[s] as arguments.
    with upytest.raises(ValueError):
        with upytest.raises():
            pass
    # Expected exception must be a subclass of BaseException.
    with upytest.raises(TypeError):
        with upytest.raises("not a BaseException"):
            pass


def test_raises_exception_passes():
    """
    Test that the expected exception is raised, and so the test will pass.
    """
    with upytest.raises(ValueError):
        raise ValueError("This is a ValueError")


def test_does_not_raise_exception_fails():
    """
    Test that the expected exception is not raised. This test will fail.
    """
    with upytest.raises(ValueError):
        pass


def test_does_not_raise_expected_exception_fails():
    """
    Test when the wrong exception is raised. This test will fail.
    """
    with upytest.raises(ValueError, AssertionError):
        raise TypeError("This is a TypeError")


class TestClass:
    """
    A class based version of the above tests.
    """

    @upytest.skip("This test will be skipped")
    def test_in_class_skipped(self):
        assert False  # This will not be executed.

    @upytest.skip(
        "This test will be skipped with a skip_when condition", skip_when=True
    )
    def test_in_class_when_skipped(self):
        assert False  # This will not be executed.

    @upytest.skip(
        "This test will NOT be skipped with a False-y skip_when",
        skip_when=False,
    )
    def test_in_class_when_not_skipped_passes(self):
        assert True, "This test passes"

    def test_in_class_passes(self):
        assert True, "This test passes"

    def test_in_class_fails(self):
        assert False, "This test will fail"

    def test_in_class_raises_exception_passes(self):
        with upytest.raises(ValueError):
            raise ValueError("This is a ValueError")

    def test_in_class_does_not_raise_exception_fails(self):
        with upytest.raises(ValueError):
            pass

    def test_in_class_does_not_raise_expected_exception_fails(self):
        with upytest.raises(ValueError, AssertionError):
            raise TypeError("This is a TypeError")


# Async versions of the above.


@upytest.skip("This async test will be skipped")
async def test_async_skipped():
    assert False  # This will not be executed.


@upytest.skip(
    "This test will be skipped with a skip_when condition", skip_when=True
)
async def test_async_when_skipped():
    assert False  # This will not be executed.


@upytest.skip(
    "This test will NOT be skipped with a False-y skip_when",
    skip_when=False,
)
async def test_async_when_not_skipped_passes():
    assert True, "This async test passes"


async def test_async_passes():
    assert True, "This async test passes."


async def test_async_fails():
    assert False, "This async test fails."


async def test_async_raises_exception_passes():
    with upytest.raises(ValueError):
        raise ValueError("This is a ValueError")


async def test_async_does_not_raise_exception_fails():
    with upytest.raises(ValueError):
        pass


async def test_async_does_not_raise_expected_exception_fails():
    with upytest.raises(ValueError, AssertionError):
        raise TypeError("This is a TypeError")


class TestAsyncClass:
    """
    An asynchronous class based version of the above tests.
    """

    @upytest.skip("This test will be skipped")
    async def test_async_in_class_skipped(self):
        assert False  # This will not be executed.

    @upytest.skip(
        "This test will be skipped with a skip_when condition", skip_when=True
    )
    async def test_async_in_class_when_skipped(self):
        assert False  # This will not be executed.

    @upytest.skip(
        "This test will NOT be skipped with a False-y skip_when",
        skip_when=False,
    )
    async def test_async_in_class_when_not_skipped_passes(self):
        assert True, "This test passes"

    async def test_async_in_class_passes(self):
        assert True, "This test passes"

    async def test_async_in_class_fails(self):
        assert False, "This test will fail"

    async def test_async_in_class_raises_exception_passes(self):
        with upytest.raises(ValueError):
            raise ValueError("This is a ValueError")

    async def test_async_in_class_does_not_raise_exception_fails(self):
        with upytest.raises(ValueError):
            pass

    async def test_async_in_class_does_not_raise_expected_exception_fails(self):
        with upytest.raises(ValueError, AssertionError):
            raise TypeError("This is a TypeError")