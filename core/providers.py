import requests
from abc import ABC, abstractmethod
from core.config import Config
from prompts.system import RUTHLESS_SYSTEM

class BaseLLMProvider(ABC):
    """Abstract base class for all LLM providers."""
    
    @abstractmethod
    def generate(self, user_text: str) -> str:
        pass


class OpenAICompatibleProvider(BaseLLMProvider):
    """
    Since Groq, OpenAI, OpenRouter, and Ollama all use the exact same 
    JSON schema, we can write the HTTP logic once.
    """
    def __init__(self, api_url: str, api_key: str, model: str):
        self.api_url = api_url
        self.api_key = api_key
        self.model = model

    def generate(self, user_text: str) -> str:
        if not self.api_key:
            raise ValueError(f"API key missing for {self.__class__.__name__}")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": RUTHLESS_SYSTEM},
                {"role": "user", "content": user_text}
            ],
            "temperature": 0.2
        }

        response = requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"API Failure [{response.status_code}]: {response.text}")

        return response.json()["choices"][0]["message"]["content"]


class GroqProvider(OpenAICompatibleProvider):
    def __init__(self):
        super().__init__(
            api_url="https://api.groq.com/openai/v1/chat/completions",
            api_key=Config.GROQ_API_KEY,
            model="llama-3.3-70b-versatile"  # Groq's free tier heavy-lifter
        )


class OpenAIProvider(OpenAICompatibleProvider):
    def __init__(self):
        super().__init__(
            api_url="https://api.openai.com/v1/chat/completions",
            api_key=Config.OPENAI_API_KEY,
            model="gpt-4o-mini"
        )


# The Factory function that returns the active provider
def get_provider() -> BaseLLMProvider:
    if Config.ACTIVE_PROVIDER == "groq":
        return GroqProvider()
    elif Config.ACTIVE_PROVIDER == "openai":
        return OpenAIProvider()
    else:
        raise ValueError(f"Unknown provider: {Config.ACTIVE_PROVIDER}")