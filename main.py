import os
from dotenv import load_dotenv
from google import genai
from search import search_properties  # Keep your existing search logic

load_dotenv()

# Initialize the Gemini Client
# It automatically looks for an environment variable named 'GEMINI_API_KEY'
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_gemini_response(query, max_price=None):
    # 1. Retrieve the compressed listings from your local index
    results = search_properties(query, max_price=max_price)

    if not results:
        return "I couldn't find any properties matching those criteria right now."

    # 2. Build context using your ScaleDown-compressed descriptions
    # This saves tokens and makes the response faster
    context_list = []
    for r in results:
        details = f"Property: {r['title']} | Price: ${r['metadata']['price']} | Info: {r['compressed_description']}"
        context_list.append(details)

    context_text = "\n".join(context_list)

    # 3. Create the prompt
    prompt = f"""
    You are a professional real estate assistant. Use the following compressed 
    property listings to answer the user's request. 
    
    User Query: {query}
    
    Listings:
    {context_text}
    
    Provide a helpful summary of the best matches.
    """

    # 4. Generate the response using Gemini 2.5 Flash
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return response.text


if __name__ == "__main__":
    user_input = "I need a cozy home with vintage charm under $700k."
    print(generate_gemini_response(user_input, max_price=700000))
