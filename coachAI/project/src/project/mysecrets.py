from dotenv import load_dotenv
import os

load_dotenv()

class Secrets:
    gemini_api_key = os.getenv("gemini_api_key")
    gemini_api_model = os.getenv("gemini_model")
    base_url = os.getenv("base_url")