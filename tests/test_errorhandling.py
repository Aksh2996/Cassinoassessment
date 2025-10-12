# tests/test_errorhandling.py
def test_resource_not_found(jsonplaceholder_helper):
    r = jsonplaceholder_helper.get("/posts/99999")
    assert r.status_code == 404

def test_method_not_allowed(httpbin_helper):
    r = httpbin_helper.delete("/status/405")
    assert r.status_code == 405
