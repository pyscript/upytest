from pyscript import window


def setup():
    window.console.log("Setup from inner conftest.py")


def teardown():
    window.console.log("Teardown from inner conftest.py")