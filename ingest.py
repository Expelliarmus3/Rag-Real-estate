import json
import os
from dotenv import load_dotenv
import scaledown as sd

load_dotenv()
sd.set_api_key(os.getenv("SCALEDOWN_API_KEY"))

# 1. Load your raw data
with open("properties.json", "r") as f:
    properties = json.load(f)

compressor = sd.ScaleDownCompressor(target_model="gpt-4o", rate="auto")
processed_data = []

print(f"--- Compressing {len(properties)} Listings ---")

for p in properties:
    result = compressor.compress(
        context=p["description"],
        prompt="Extract key architectural features and neighborhood vibe for search indexing.",
    )

    # Store the original metadata + the NEW compressed description
    p["compressed_description"] = result.content
    processed_data.append(p)
    print(f"Done: {p['title']}")

# 2. Save the NEW 'Dense' Database
with open("processed_properties.json", "w") as f:
    json.dump(processed_data, f, indent=4)

print("\nSuccess! 'processed_properties.json' is ready for your search system.")
