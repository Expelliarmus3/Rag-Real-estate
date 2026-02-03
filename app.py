import os
from dotenv import load_dotenv
import scaledown as sd

load_dotenv()  # This looks for the .env file and loads your keys
sd.set_api_key(os.getenv("SCALEDOWN_API_KEY"))

print("Setup complete! ScaleDown is ready.")
