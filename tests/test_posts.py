import requests

def test_get_posts(api_url):
    """Test fetching all posts."""
    response = requests.get(f"{api_url}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_post(api_url):
    """Test fetching a single post."""
    post_id = 1
    response = requests.get(f"{api_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id
