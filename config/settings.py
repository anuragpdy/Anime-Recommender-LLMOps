import os
from dotenv import load_dotenv

load_dotenv()

# API and Model Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# File Path Configuration
RAW_DATA_PATH = "data/raw/anime_with_synopsis.csv"
PROCESSED_DATA_PATH = "data/processed/anime_updated.csv"
VECTOR_DB_PATH = "chroma_db"