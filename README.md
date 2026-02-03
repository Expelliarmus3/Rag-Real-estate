# 🏠 SmartEstate: Optimized Real Estate RAG Search
A high-performance, cost-effective property search system built using Retrieval-Augmented Generation (RAG). This project leverages ScaleDown for intelligent context compression and Google Gemini for natural language response generation, significantly reducing token costs while maintaining search accuracy.

## 🚀 The Innovation: Context Compression
Traditional RAG systems are expensive because real estate listings are "wordy." By using the ScaleDown framework, this system "shrinks" raw descriptions into dense, semantic summaries before indexing them.

Cost Reduction: ~60-80% lower embedding and storage costs.

Speed: Faster retrieval and lower latency for LLM generations.

Precision: Hybrid search combining hard metadata (price, beds) with compressed semantic "vibes."

## 🛠️ Tech Stack
LLM: Google Gemini 2.5 Flash

Compression: ScaleDown (Python Framework)

Backend: Python 3.10+

Data: JSON-based local vector store (easily upgradable to Pinecone/Milvus)

## 📂 Project Structure

real-estate-search/
├── data/
│   ├── properties.json           # Raw property data
│   └── processed_properties.json # Compressed 'Dense' database
├── src/
│   ├── ingestion.py              # ScaleDown compression logic
│   ├── search.py                 # Hybrid filtering & retrieval
│   └── main.py                   # Gemini RAG generation
├── .env                          # API Keys (Protected)
└── requirements.txt              # Project dependencies
## ⚙️ Setup & Installation
1. Clone & Link ScaleDown
Since ScaleDown is a local dependency, link it to your project:

Bash
### Navigate to your local ScaleDown clone
| cd path/to/scaledown
| pip install -e .

### Navigate back to this project
| cd path/to/real-estate-search
| pip install google-genai python-dotenv
  
2. Configure Environment Variables
   
Create a .env file in the root directory:

Plaintext
| SCALEDOWN_API_KEY=your_scaledown_key
| GEMINI_API_KEY=your_gemini_key
  
3. Run Ingestion
   
Compress your raw data into the optimized search index:

Bash
| python src/ingestion.py
  
4. Search & Ask
   
Run the main RAG application to query the database:

Bash

| python src/main.py

🔍 How it Works

Ingestion: ScaleDownCompressor processes long listings into searchable fragments.

Retrieval: The system performs a case-insensitive keyword match on the compressed text while applying hard metadata filters (e.g., Price < $900k).

Generation: The top matching listings are passed as a "dense context" to Gemini 2.5 Flash, which provides a conversational recommendation.

📈 Future Roadmap

[] Vector DB Integration: Move from local JSON to Milvus for million-scale listings.

[] Fuzzy Search: Implement thefuzz for better keyword matching (e.g., "garden" matching "backyard").

[] Web UI: Build a Streamlit dashboard for interactive searching.
