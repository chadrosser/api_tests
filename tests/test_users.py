import requests

def test_get_users(api_url):
    """Test fetching all users."""
    response = requests.get(f"{api_url}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_user(api_url):
    """Test fetching a single user."""
    user_id = 1
    response = requests.get(f"{api_url}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id
