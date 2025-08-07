from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="anime_recommender",
    version="0.1.0",
    author="Anurag PAndey",
    description="An AI-powered anime recommender system.",
    long_description="A RAG-based anime recommender using Streamlit, LangChain, and Groq.",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)