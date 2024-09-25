"""
pytest conftest file with fixtures for acceptance tests
"""

import time

import box
import pytest
import requests
import timeout_decorator

import net.config
import net.initialization
import net.utilities


@pytest.fixture(scope="function")
def test_config() -> box.Box:
    """
    Load the test configuration
    """

    return net.utilities.get_config("/configurations/development_config.yaml")


@pytest.fixture(scope="session")
def session_scoped_test_config() -> box.Box:
    """
    Load the test configuration
    """

    return net.utilities.get_config("/configurations/development_config.yaml")


@pytest.fixture(scope="session")
def wait_on_supertokens_core(session_scoped_test_config):
    """
    Wait for supertokens core to be ready to accept requests
    """

    @timeout_decorator.timeout(30)
    def probe():

        is_ready = False

        import icecream

        while is_ready is False:

            time.sleep(0.1)

            icecream.ic(session_scoped_test_config.supertokens_core.docker_network.url)

            try:
                response = requests.get(
                    session_scoped_test_config.supertokens_core.docker_network.url + "/hello",
                    timeout=5
                )

                is_ready = response.status_code == 200

            except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
                pass

    probe()


@pytest.fixture(scope="function")
def clean_supertokens_data(wait_on_supertokens_core, test_config):
    """
    Clean supertokens data
    """

    _ = wait_on_supertokens_core

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
