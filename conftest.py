import pytest
from utils.general_fixtures import *


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environments to run test: dev or qa"
    )


@pytest.fixture(scope="session")
def env(pytestconfig):
    valid_env_list = ["dev", "qa"]
    given_env = pytestconfig.getoption("env").lower()
    assert given_env in valid_env_list, f"Not a valid environment - Valid environments: {valid_env_list}"
    return given_env
