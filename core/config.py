import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ACTIVE_PROVIDER = os.getenv("ACTIVE_PROVIDER", "groq").lower()