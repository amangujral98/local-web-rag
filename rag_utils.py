from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

OLLAMA_BASE_URL = "http://127.0.0.1:11434"
CHAT_MODEL = "llama3.1"
EMBED_MODEL = "nomic-embed-text"
CHROMA_DIR = "chroma_db"


def load_and_split_webpage(url):

    loader = WebBaseLoader(url)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    splits = splitter.split_documents(docs)

    return splits


def build_vectorstore(documents):

    embeddings = OllamaEmbeddings(
        model=EMBED_MODEL,
        base_url=OLLAMA_BASE_URL
    )

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    return vectorstore


def get_retriever(vectorstore):

    return vectorstore.as_retriever(search_kwargs={"k": 4})


def format_docs(docs):

    return "\n\n".join(doc.page_content for doc in docs)


def ask_llm(question, context):

    llm = ChatOllama(
        model=CHAT_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0
    )

    prompt = f"""
Answer the question using ONLY the context below.

Question:
{question}

Context:
{context}
"""

    response = llm.invoke(prompt)

    return response.content.strip()


def run_rag(question, retriever):

    docs = retriever.invoke(question)

    context = format_docs(docs)

    answer = ask_llm(question, context)

    return answer, docs