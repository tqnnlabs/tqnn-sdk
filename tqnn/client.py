import requests


class TQNNClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def run_any(self, data, mode="ANY", label=None, metadata=None, sfreq=None):
        payload = {
            "data": data,
            "mode": mode,
            "label": label,
            "metadata": metadata or {},
            "sfreq": sfreq,
        }

        response = requests.post(
            f"{self.base_url}/run/any",
            json=payload,
            headers={
                "x-api-key": self.api_key,
                "Content-Type": "application/json",
            },
            timeout=120,
        )

        response.raise_for_status()
        return response.json()
