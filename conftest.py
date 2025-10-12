# conftest.py
import pytest, yaml
from helpers.reqres_helper import ReqresHelper
from helpers.jsonplaceholder_helper import JsonPlaceholderHelper
from helpers.httpbin_helper import HttpBinHelper
from helpers.gorest_helper import GoRestHelper

def load_config():
    with open("config/config.yaml") as f:
        cfg = yaml.safe_load(f)
    env = cfg.get("env", "dev")
    return cfg[env]

cfg = load_config()

@pytest.fixture(scope="session")
def reqres_helper():
    return ReqresHelper(cfg["REQRES_BASE"])

@pytest.fixture(scope="session")
def jsonplaceholder_helper():
    return JsonPlaceholderHelper(cfg["JSONPLACEHOLDER_BASE"])

@pytest.fixture(scope="session")
def httpbin_helper():
    return HttpBinHelper(cfg["HTTPBIN_BASE"])

@pytest.fixture(scope="session")
def gorest_helper():
    return GoRestHelper(cfg["GOREST_BASE"], cfg["GOREST_TOKEN"])
