import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document

st.set_page_config(page_title="File Q&A with OpenAI", layout="wide")
st.title("✍️ File Q&A with OpenAI") # Changed title and icon to match


def read_file(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    return ""

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return [Document(page_content=chunk) for chunk in splitter.split_text(text)]


st.markdown("Upload a file to get started")

# File uploader section 
uploaded_files = st.file_uploader(
    "Drag and drop file here\n\nLimit 200MB per file • TXT, MD (Showing supported types)",
    type=["txt", "pdf"], # Keeping functional types
    accept_multiple_files=True,
    key="file_uploader"
)

# Initialize session_state 
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "retriever" not in st.session_state:
    st.session_state.retriever = None

# Process uploaded files
if uploaded_files and st.session_state.vectorstore is None:
    # Use a spinner to show the processing time
    with st.spinner("Processing files..."):
        all_chunks = []
        for f in uploaded_files:
            text = read_file(f)
            chunks = chunk_text(text)
            for chunk in chunks:
                chunk.metadata = {"source": f.name}
            all_chunks.extend(chunks)
        
        # Create embeddings and vectorstore
        embeddings = OpenAIEmbeddings(model="openai.text-embedding-3-large")
        st.session_state.vectorstore = Chroma.from_documents(documents=all_chunks, embedding=embeddings)
        st.session_state.retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3})
    
    st.success(f"✅ Loaded {len(uploaded_files)} file(s), created {len(all_chunks)} chunks total. Vector store ready!")

# Display  prompt
st.markdown("---") 
st.markdown("## 🟧 Ask something about the Uploaded File")

# Display a message if no files are processed yet
if st.session_state.retriever is None:
    st.info("Upload files above to start asking questions.")
    
#Display chat history
if st.session_state.chat_history:
    st.subheader("💬 Conversation")
    # Display chat history (reversed for latest at the bottom)
    for q, a, docs in st.session_state.chat_history: # Display in order for chat flow
        with st.chat_message("user"):
            st.markdown(q)
        with st.chat_message("assistant"):
            st.markdown(a)
            
#Retrieval and Generation
if st.session_state.retriever:
    chat_input_container = st.container()
    
    with chat_input_container:
        llm = ChatOpenAI(model_name="openai.gpt-4o", temperature=0.2)
        question = st.chat_input("Ask something about the article")

        if question:
            # Retrieval
            docs = st.session_state.retriever.get_relevant_documents(question)
            context = "\n\n".join([d.page_content for d in docs])
            
            prompt = f"Answer the question based on the context below.\n\nContext:\n{context}\n\nQuestion: {question}"
            response = llm.invoke(prompt)
            
            # Save chat
            st.session_state.chat_history.append((question, response.content, docs))
            
            # Rerun to update the history display immediately
            st.rerun()