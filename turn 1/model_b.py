import time
import random
import pytest

@pytest.fixture(scope="function")
def slow_server():
    # Simulate starting the slow server
    print("Starting slow server...")
    time.sleep(2)  # Replace this with actual server startup time
    yield
    # Simulate stopping the slow server
    print("Stopping slow server...")

@pytest.fixture(scope="function")
def random_value():
    # Generate a random value that the test relies on
    return random.randint(1, 100)

@pytest.mark.flaky(reruns=3)
def test_flaky_api_call(slow_server, random_value):
    # Make an API call to the slow server using the random value
    response = make_api_call(random_value)

    # Assertions to validate the response
    assert response.status_code == 200
    assert random_value in response.text
