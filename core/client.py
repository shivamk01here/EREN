import requests

from core.config import config


class Client:
    def __init__(self):
        config.validate()
        self.url = config.ANTHROPIC_API_URL
        self.headers = {
            "x-api-key": config.ANTHROPIC_API_KEY,
            "anthropic-version": config.ANTHROPIC_API_VERSION,
            "content-type": "application/json",
        }

    def send(self, system_prompt: str, messages: list[dict]) -> str:
        payload = {
            "model": config.ANTHROPIC_MODEL,
            "max_tokens": config.MAX_TOKENS,
            "system": system_prompt,
            "messages": messages,
        }

        response = requests.post(self.url, headers=self.headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()

        return "".join(block["text"] for block in data["content"] if block["type"] == "text")
