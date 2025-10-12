from jsonschema import validate


def test_login_schema(reqres_helper):
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    r = reqres_helper.post("/login", payload)

    # If API key required, check correct error message
    if r.status_code == 401:
        data = r.json()
        assert "error" in data
        assert data["error"].lower() in ["missing api key", "unauthorized"]
    else:
        # Old behavior: should contain token
        assert r.status_code in [200, 201]
        schema = {
            "type": "object",
            "properties": {"token": {"type": "string"}},
            "required": ["token"]
        }
        validate(instance=r.json(), schema=schema)
