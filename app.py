import streamlit as st
from rag_utils import load_and_split_webpage, build_vectorstore, get_retriever, run_rag

st.title("Chat with Webpage using Local Llama 3.1")

if "retriever" not in st.session_state:
    st.session_state.retriever = None

url = st.text_input("Enter webpage URL")

if st.button("Load Webpage"):

    docs = load_and_split_webpage(url)

    vectorstore = build_vectorstore(docs)

    retriever = get_retriever(vectorstore)

    st.session_state.retriever = retriever

    st.success("Webpage loaded successfully")

if st.session_state.retriever:

    question = st.text_input("Ask a question")

    if st.button("Get Answer"):

        answer, docs = run_rag(question, st.session_state.retriever)

        st.write(answer)

        with st.expander("Retrieved context"):
            for d in docs:
                st.write(d.page_content)