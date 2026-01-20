import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="News Analyst AI",
    page_icon="📰",
    layout="wide"
)

load_dotenv()

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    """
    <h1 style='text-align: center;'>📰 News Analyst Chatbot</h1>
    <p style='text-align: center; color: gray;'>
    Ask intelligent questions across multiple news articles
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# Sidebar - URL Input
# --------------------------------------------------
with st.sidebar:
    st.header("🔗 News Sources")
    st.caption("Add up to 3 news article URLs")

    urls = []
    for i in range(3):
        url = st.text_input(f"Article URL {i+1}", placeholder="https://...")
        if url:
            urls.append(url)

    process_btn = st.button("🚀 Process Articles", use_container_width=True)

# --------------------------------------------------
# LLM
# --------------------------------------------------
llm = OpenAI(temperature=0, max_tokens=500)
embeddings = OpenAIEmbeddings()

# --------------------------------------------------
# Processing Section
# --------------------------------------------------
status_box = st.empty()

if process_btn:
    if not urls:
        st.error("⚠️ Please enter at least one valid URL")
        st.stop()

    with status_box.container():
        with st.spinner("📥 Loading articles..."):
            loader = UnstructuredURLLoader(urls=urls)
            data = loader.load()

        with st.spinner("✂️ Splitting content..."):
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            docs = splitter.split_documents(data)

        with st.spinner("🧠 Creating knowledge base..."):
            vectorstore = FAISS.from_documents(docs, embeddings)
            vectorstore.save_local("faiss_index")

        st.success("✅ Articles indexed successfully!")

# --------------------------------------------------
# Chat Section
# --------------------------------------------------
st.divider()
st.subheader("💬 Ask Questions")

if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.chat_input("Ask something about the articles...")

if query:
    st.session_state.chat.append(("user", query))

    if os.path.exists("faiss_index"):
        vectorstore = FAISS.load_local("faiss_index", embeddings)

        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )

        with st.spinner("🤖 Thinking..."):
            result = chain({"question": query}, return_only_outputs=True)

        answer = result["answer"]
        sources = result.get("sources", "")

        st.session_state.chat.append(("bot", answer, sources))

# --------------------------------------------------
# Render Chat
# --------------------------------------------------
for msg in st.session_state.chat:
    if msg[0] == "user":
        with st.chat_message("user"):
            st.write(msg[1])
    else:
        with st.chat_message("assistant"):
            st.write(msg[1])

            if msg[2]:
                with st.expander("🔍 Sources"):
                    for s in msg[2].split("\n"):
                        st.write(s)
