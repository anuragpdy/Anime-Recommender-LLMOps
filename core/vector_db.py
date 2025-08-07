from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from config.settings import EMBEDDING_MODEL_NAME

class VectorStoreBuilder:
    """Handles the creation and loading of the Chroma vector store."""

    def __init__(self, csv_path: str = None, persist_dir: str = "chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    def build_and_save(self):
        """Builds the vector store from a CSV and saves it to disk."""
        if not self.csv_path:
            raise ValueError("CSV path must be provided to build the vector store.")

        loader = CSVLoader(
            file_path=self.csv_path,
            encoding='utf-8',
            metadata_columns=[]
        )
        data = loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        db = Chroma.from_documents(texts, self.embedding, persist_directory=self.persist_dir)
        db.persist()

    def load_vector_store(self):
        """Loads a persisted vector store from disk."""
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding)