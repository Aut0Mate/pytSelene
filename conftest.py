import pytest

from utils.driver_utils.init_driver import initialize_driver, quit_driver


@pytest.fixture(scope="session", autouse=True)
def driver():
    yield initialize_driver()
    quit_driver()
