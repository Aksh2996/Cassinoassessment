# tests/test_performance.py
import time, concurrent.futures

def test_response_time(jsonplaceholder_helper):
    start = time.time()
    r = jsonplaceholder_helper.get("/posts/1")
    assert r.status_code == 200
    assert (time.time() - start) < 1.0

def test_concurrent_requests(httpbin_helper):
    def make_request():
        r = httpbin_helper.get("/delay/1")
        return r.status_code

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        futures = [ex.submit(make_request) for _ in range(10)]
        results = [f.result() for f in futures]
    assert all(s == 200 for s in results)
