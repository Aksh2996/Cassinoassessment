# helpers/jsonplaceholder_helper.py
import requests, logging, os

os.makedirs("logs", exist_ok=True)
logger = logging.getLogger("api_helpers")

class JsonPlaceholderHelper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        resp = requests.get(url)
        logger.info(f"RESP {resp.status_code} | {resp.text}")
        return resp

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} | payload={payload}")
        resp = requests.post(url, json=payload)
        logger.info(f"RESP {resp.status_code} | {resp.text}")
        return resp
