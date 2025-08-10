import streamlit as st
from core.recommender import AnimeRecommender
from core.vector_db import VectorStoreBuilder
from config.settings import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger


# Initialize logger
logger = get_logger(__name__)

st.set_page_config(page_title="Anime Recommender", layout="wide")

@st.cache_resource
def init_recommender():
    """
    Initializes the recommender system with detailed logging checkpoints.
    """
    st.info("Starting recommender system initialization...")
    logger.info("Starting recommender system initialization...")

    try:
        st.info("Step 1: Initializing VectorStoreBuilder...")
        logger.info("Step 1: Initializing VectorStoreBuilder...")
        vector_builder = VectorStoreBuilder(persist_dir="chroma_db")
        st.info("✅ VectorStoreBuilder initialized.")
        logger.info("✅ VectorStoreBuilder initialized.")

        st.info("Step 2: Loading vector store from disk... (This may take a moment)")
        logger.info("Step 2: Loading vector store from disk...")
        vector_store = vector_builder.load_vector_store()
        st.info("✅ Vector store loaded.")
        logger.info("✅ Vector store loaded.")

        st.info("Step 3: Creating retriever...")
        logger.info("Step 3: Creating retriever...")
        retriever = vector_store.as_retriever()
        st.info("✅ Retriever created.")
        logger.info("✅ Retriever created.")

        st.info("Step 4: Initializing AnimeRecommender...")
        logger.info("Step 4: Initializing AnimeRecommender...")
        recommender = AnimeRecommender(
            retriever=retriever,
            api_key=GROQ_API_KEY,
            model_name=MODEL_NAME
        )
        st.info("✅ AnimeRecommender initialized.")
        logger.info("✅ AnimeRecommender initialized.")

        st.success("Recommender system initialized successfully!")
        logger.info("Recommender system initialized successfully!")
        return recommender

    except Exception as e:
        logger.error(f"Failed to initialize recommender: {e}")
        st.error(f"Could not initialize the recommendation engine: {e}")
        return None

# Main app logic
st.title("Anime Recommender System")

recommender = init_recommender()

if recommender:
    st.info("Initialization complete. Ready for your query.")
    query = st.text_input("Enter your anime preferences (e.g., 'a funny anime about space pirates')")

    if query:
        with st.spinner("Fetching recommendations for you..."):
            try:
                response = recommender.get_recommendation(query)
                st.markdown("### Here are your recommendations:")
                st.write(response)
                logger.info(f"Successfully generated recommendation for query: '{query}'")
            except Exception as e:
                logger.error(f"Failed to get recommendation for query '{query}': {e}")
                # Show the actual error in the UI for debugging
                st.error(f"An error occurred: {e}") 