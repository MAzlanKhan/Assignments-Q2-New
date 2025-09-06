from dotenv import load_dotenv
import os

load_dotenv()

class Secrets:
    def __init__(self):
        self.gemini_api_key = os.getenv("gemini_api_key")
        self.gemini_api_model = os.getenv("gemini_api_model")
        self.base_url = os.getenv("base_url")