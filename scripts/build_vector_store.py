from core.data_processing import AnimeDataProcessor
from core.vector_db import VectorStoreBuilder
from config.settings import RAW_DATA_PATH, PROCESSED_DATA_PATH, VECTOR_DB_PATH
from utils.logger import get_logger
from utils.custom_exceptions import CustomException


logger = get_logger(__name__)

def main():
    """
    Main script to build the entire data pipeline:
    1. Processes raw data.
    2. Builds and saves the vector store.
    """
    try:
        logger.info("Starting to build the data pipeline...")

        # 1. Process the raw data from the paths defined in our settings
        logger.info("Loading and processing data...")
        processor = AnimeDataProcessor(
            raw_csv_path=RAW_DATA_PATH,
            processed_csv_path=PROCESSED_DATA_PATH
        )
        processed_csv = processor.process()
        logger.info(f"Data processed and saved to {processed_csv}")

        # 2. Build and save the vector store from the processed data
        logger.info("Building vector store...")
        vector_builder = VectorStoreBuilder(
            csv_path=processed_csv,
            persist_dir=VECTOR_DB_PATH
        )
        vector_builder.build_and_save()
        logger.info("Vector store built successfully.")

        logger.info("Pipeline built successfully!")

    except Exception as e:
        logger.error(f"Failed to execute pipeline: {str(e)}")
        raise CustomException("Error during pipeline execution", e)

if __name__ == "__main__":
    main()