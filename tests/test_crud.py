# tests/test_crud.py
def test_create_post(jsonplaceholder_helper):
    payload = {"title": "Test Post", "body": "Content", "userId": 1}
    r = jsonplaceholder_helper.post("/posts", payload)
    assert r.status_code == 201
    assert r.json().get("id") == 101

def test_get_post(jsonplaceholder_helper):
    r = jsonplaceholder_helper.get("/posts/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1
