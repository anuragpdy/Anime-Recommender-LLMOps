from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

class AnimeRecommender:
    """Handles the core logic for generating anime recommendations."""

    PROMPT_TEMPLATE = """
                    You are an expert anime recommender. Your job is to help users find the perfect anime based on their preferences.

                    Using the following context, provide a detailed and engaging response to the user's question.

                    For each question, suggest exactly three anime titles. For each recommendation, include:
                    1. The anime title.
                    2. A concise plot summary (2-3 sentences).
                    3. A clear explanation of why this anime matches the user's preferences.

                    Present your recommendations in a numbered list format for easy reading.

                    If you don't know the answer, respond honestly by saying you don't know — do not fabricate any information.

                    Context:
                    {context}

                    User's question:
                    {question}

                    Your well-structured response:
                    """

    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = PromptTemplate(
            template=self.PROMPT_TEMPLATE,
            input_variables=["context", "question"]
        )
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def get_recommendation(self, query: str) -> str:
        """
        Generates a recommendation based on the user's query.
        """
        result = self.qa_chain({"query": query})
        return result['result']

