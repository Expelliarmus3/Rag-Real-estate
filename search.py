import json


def load_data():
    with open("processed_properties.json", "r") as f:
        return json.load(f)


def search_properties(query_text, max_price=None, min_beds=None):
    properties = load_data()
    results = []

    # Standardize the search text for case-insensitivity
    query_text = query_text.lower()

    for p in properties:
        # 1. Hard Metadata Filtering (Fast)
        if max_price and p["metadata"]["price"] > max_price:
            continue
        if min_beds and p["metadata"]["beds"] < min_beds:
            continue

        # 2. Keyword Match in Compressed Description (Smart)
        # We search the SHRUNKEN text produced by ScaleDown
        if (
            query_text in p["compressed_description"].lower()
            or query_text in p["title"].lower()
        ):
            results.append(p)

    return results


# Example Test Run
if __name__ == "__main__":
    print("--- Real Estate Search ---")
    user_query = "garden"  # Try 'modern', 'garden', or 'historic'

    found = search_properties(user_query, max_price=900000, min_beds=2)

    print(f"Found {len(found)} results for '{user_query}':")
    for item in found:
        print(f"- {item['title']} (${item['metadata']['price']})")
        print(f"  Snippet: {item['compressed_description'][:75]}...")
