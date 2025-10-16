**📚 RAG-Powered File Q&A with Streamlit and LangChain**

A Streamlit app that lets users upload **PDF or text files** and **ask questions** about their content using **LangChain**, **Chroma**, and **OpenAI’s GPT-4o**.  
The app embeds documents, retrieves relevant text, and generates answers in an interactive chat.

---

### Features Overview

- **Multi-File Upload:** Supports uploading multiple files in TXT and PDF formats.

- **Document Preprocessing:** Uses PyPDF2 for PDF extraction and RecursiveCharacterTextSplitter to break down documents into manageable chunks.

- **Vector Storage:** Leverages OpenAI Embeddings to convert text chunks into vectors and stores them in a Chroma vector database for efficient semantic searching.

- **Contextual Q&A:** A retriever fetches the most relevant document chunks based on the user's question, and these chunks are passed as context to the gpt-4o large language model.

- **Chat Interface:** Maintains conversation flow and displays history.

## Design Choices
- **Chunking:** Split documents by sentence boundaries with overlap to preserve context.
- **Retrieval:** Used FAISS for efficient similarity search across multiple document vectors.
- **Language Model:** Used OpenAI GPT-4.o for grounded answers based on retrieved text.
- **Interface:** Implemented with Streamlit for simplicity and fast iteration.
- **Multi-document Support:** Each chunk stores document metadata to track source.

## ⚙️ Setup

