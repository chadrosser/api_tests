import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_url():
    return BASE_URL