# tests/test_gorest.py
import random, string, pytest

def random_email():
    return f"user_{''.join(random.choices(string.ascii_lowercase, k=6))}@example.com"

@pytest.fixture
def created_user_id(gorest_helper):
    payload = {"name": "Temp User", "email": random_email(), "gender":"male", "status":"active"}
    r = gorest_helper.post("/users", payload)
    assert r.status_code == 201
    uid = r.json()["id"]
    yield uid
    # cleanup
    gorest_helper.delete(f"/users/{uid}")

def test_create_user(gorest_helper, created_user_id):
    # created_user_id fixture asserts creation already
    assert isinstance(created_user_id, int)

def test_invalid_email(gorest_helper):
    payload = {"name":"X", "email":"bad-email", "gender":"male","status":"active"}
    r = gorest_helper.post("/users", payload)
    assert r.status_code == 422
