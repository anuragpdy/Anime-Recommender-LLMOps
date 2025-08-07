# Parent image
FROM python:3.10-slim

# Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Work directory inside the docker container
WORKDIR /app

# Installing system dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copying requirements and installing packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying all other contents from local to app
COPY . .

# Run the data processing script to build the vector store
RUN python scripts/build_vector_store.py

# Used PORTS
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app/web_ui.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]