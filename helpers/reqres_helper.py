# helpers/reqres_helper.py
import requests, logging, os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("api_helpers")
if not logger.handlers:
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("logs/api.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

class ReqresHelper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url} | params={params}")
        resp = requests.get(url, params=params)
        logger.info(f"RESP {resp.status_code} | {resp.text}")
        return resp

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} | payload={payload}")
        resp = requests.post(url, json=payload)
        logger.info(f"RESP {resp.status_code} | {resp.text}")
        return resp
