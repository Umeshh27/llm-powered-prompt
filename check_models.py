import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROK_API_KEY")

response = requests.get(
    "https://api.x.ai/v1/models",
    headers={
        "Authorization": f"Bearer {API_KEY}"
    }
)

print(response.json())