import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROK_API_KEY")

try:
    response = requests.get(
        "https://api.x.ai/v1/models",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    with open("models.json", "w") as f:
        json.dump(response.json(), f, indent=2)
except Exception as e:
    with open("models.json", "w") as f:
        f.write(str(e))
