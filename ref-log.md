# Reference Log (`ref-log.md`)

## 🔗 External Tools and Libraries

| Tool / Library | Purpose | Description |
|----------------|----------|-------------|
| **Streamlit** | Web application framework | Utilized to develop an interactive interface that allows users to upload files, visualize processing states, and interact with the question-answering system. |
| **LangChain** | Framework for retrieval-augmented generation (RAG) systems | Provided core components for text chunking, retrieval, and document management. |
| **LangChain-Community** | Community-maintained integrations for LangChain | Used for accessing the `Chroma` vector store implementation and other external modules. |
| **LangChain-OpenAI** | OpenAI model and embedding integrations for LangChain | Supplied updated and compatible interfaces for `ChatOpenAI` and `OpenAIEmbeddings`. |
| **Chroma** | Vector database | Served as the vector storage backend for document embeddings, supporting efficient semantic retrieval. |
| **OpenAI API** (`GPT-4o`, `text-embedding-3-large`) | Natural language and embedding models | Powered both text embedding generation and question-answer responses based on retrieved document context. |
| **PyPDF2** | PDF text extraction library | Enabled the extraction of text data from user-uploaded PDF documents for embedding and retrieval. |


---

## Generative AI (GenAI) Usage

| Usage Area | Tool / Model | Rationale |
|-------------|---------------|------------|
| **Documentation development** | ChatGPT | Employed to assist in refining the project’s documentation (`README.md` and `ref-log.md`) to ensure clarity, conciseness, and proper academic tone. |
| **Debugging support** | ChatGPT | Utilized to interpret deprecation warnings and suggest appropriate dependency installations. |

---

## Summary

All external sources and generative AI tools were used ethically and transparently.  
Generative AI assistance was limited to **documentation refinement**, **code compatibility updates**, and **debugging guidance**.  
All code and configurations were reviewed, verified, and tested manually to ensure correctness and alignment with project objectives.

---
