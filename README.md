# 📰 News Analyst AI Chatbot

A **Streamlit + LangChain** powered AI chatbot that allows you to analyze and ask questions across multiple news articles using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- 🌐 Add up to **3 news article URLs**
- ✂️ Automatic text splitting and embedding
- 🧠 Vector search using **FAISS**
- 🤖 Ask intelligent questions with **source citations**
- 💬 Clean chat-style interface using Streamlit
- 🔐 Environment-based API key management

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **OpenAI API**
- **FAISS Vector Store**
- **Unstructured URL Loader**
- **dotenv**

---

## 📂 Project Structure

```
.
├── app.py                # Main Streamlit application
├── faiss_index/          # Vector database (auto-generated)
├── .env                  # Environment variables
├── requirements.txt
└── README.md
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/news-analyst-ai.git
cd news-analyst-ai
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. Enter up to **3 news article URLs**
2. Click **Process Articles**
3. Articles are:
   - Loaded using `UnstructuredURLLoader`
   - Split into chunks
   - Embedded using OpenAI embeddings
   - Stored in FAISS
4. Ask questions via chat
5. AI responds with **answers + sources**

---

## 📌 Sample Questions

- *What is the main issue discussed in the article?*
- *Compare viewpoints across the articles*
- *Summarize the key findings*
- *What companies or people are mentioned?*

---

## ⚠️ Notes

- FAISS index is stored locally (`faiss_index/`)
- Re-processing articles overwrites the existing index
- Make sure URLs are publicly accessible

---

## 📈 Future Improvements

- Multi-session vector stores
- PDF & document upload support
- Better source highlighting
- Caching for faster performance
- Support for more than 3 URLs

---

## 👩‍💻 Author

**Riddhima Urankar**  
Computer Engineering Undergraduate  
AI | ML | Backend | GSoC Aspirant  

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!
