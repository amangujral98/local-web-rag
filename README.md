# Local Llama 3.1 RAG Chat App

This project is a Retrieval-Augmented Generation (RAG) application that allows users to chat with any webpage using a local Llama 3.1 model.

The application loads webpage content, converts it into embeddings, stores them in a Chroma vector database, and retrieves relevant information to answer user questions.

## Features

- Chat with any webpage
- Fully local AI (no OpenAI API required)
- Uses Llama 3.1 via Ollama
- Vector search with ChromaDB
- Built with Streamlit UI

## Tech Stack

- Llama 3.1 (Ollama)
- LangChain
- Chroma Vector Database
- Streamlit
- BeautifulSoup

## Installation

Clone the repository:

git clone https://github.com/amangujral98/local-web-rag.git

Navigate to the project folder:

cd local-web-rag

Create virtual environment:

python -m venv venv

Activate environment:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run the App

Start Ollama and make sure the models are installed:

ollama pull llama3.1
ollama pull nomic-embed-text

Run the Streamlit application:

streamlit run app.py

Open your browser at:

http://localhost:8501

## Example Usage

1. Enter a webpage URL  
2. Ask a question about the page  
3. The system retrieves relevant information and answers using Llama 3.1

## Project Structure

local-web-rag
│
├── app.py
├── rag_utils.py
├── requirements.txt
├── README.md


Connect with me for any project related help 
LinkedIn: https://www.linkedin.com/in/amandeep-singh-gujral/
