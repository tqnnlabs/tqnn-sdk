import requests


class TQNNClient:
    def __init__(self, api_key, base_url="https://tqnn-anyengine-api-914075492772.northamerica-northeast1.run.app"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def run_any(self, data, mode="ANY"):
        response = requests.post(
            f"{self.base_url}/predict",
            json={"data": data, "mode": mode},
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            timeout=60,
        )

        response.raise_for_status()
        return response.json()
