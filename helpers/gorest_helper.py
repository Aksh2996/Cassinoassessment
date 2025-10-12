# helpers/gorest_helper.py
import requests, logging, os

os.makedirs("logs", exist_ok=True)
logger = logging.getLogger("api_helpers")

class GoRestHelper:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} | payload={payload}")
        resp = requests.post(url, json=payload, headers=self.headers)
        logger.info(f"RESP {resp.status_code} | {resp.text}")
        return resp

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        resp = requests.delete(url, headers=self.headers)
        logger.info(f"RESP {resp.status_code} | {resp.text}")
        return resp
