"""
pytest conftest file with fixtures for acceptance tests
"""

import box
import pytest
import requests

import net.config
import net.initialization
import net.utilities


@pytest.fixture(scope="function")
def test_config() -> box.Box:
    """
    Load the test configuration
    """

    return net.utilities.get_config("/configurations/development_config.yaml")


@pytest.fixture(scope="function")
def clean_supertokens_data(test_config):
    """
    Clean supertokens data
    """

    # First get all the users for public app
    response = requests.get(
        test_config.supertokens_core.docker_network.url + "/users",
        timeout=5)

    response.raise_for_status()

    # Get all the users
    users = response.json()["users"]

    # Remove all the users
    for user in users:

        response = requests.post(
            test_config.supertokens_core.docker_network.url + "/user/remove",
            json={
                "userId": user["id"]
            },
            timeout=5
        )

        response.raise_for_status()


@pytest.fixture(scope="function")
def test_client():
    """
    Fixtures that returns flask test client
    """

    app = net.initialization.get_configured_app(net.config)
    return app.test_client()
