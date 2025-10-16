# 📚 INFO 5940 Assignment 1 - File Q&A with Streamlit and LangChain

A Streamlit app that lets users upload **PDF or text files** and **ask questions** about their content using **LangChain**, **Chroma**, and **OpenAI’s GPT-4o**.  
The app embeds documents, retrieves relevant text, and generates answers in an interactive chat.

---

## 1. Features Overview

- **Multi-File Upload:** Supports uploading multiple files in TXT and PDF formats.

- **Document Preprocessing:** Uses PyPDF2 for PDF extraction and RecursiveCharacterTextSplitter to break down documents into manageable chunks.

- **Vector Storage:** Leverages OpenAI Embeddings to convert text chunks into vectors and stores them in a Chroma vector database for efficient semantic searching.

- **Contextual Q&A:** A retriever fetches the most relevant document chunks based on the user's question, and these chunks are passed as context to the gpt-4o large language model.

- **Chat Interface:** Maintains conversation flow and displays history.

---

## 2. Changes in Configuration 
1. **New File - main.py:** this is the impelmentation of my code for the assignment. 

2. **PyPDF2==3.0.1** is added to 
    ```bash
   requirements.txt
   ```  

---

## 3. Setup

### Setting Your API Key in GH Codespaces
You will receive an individual API Key for class assignments. To prevent accidental exposure online, please follow the steps below to securely insert your key in the terminal.
1. **Open the terminal** inside your Codespace.
2. Run the command to temporarily set your API Key for this session:  
   ```bash
   export API_KEY="your_actual_API_KEY"
   ```
3. If you want to run the Streamlit app and set up the key at the same time, run both commands together:
   ```bash
   API_KEY="your_actual_API_KEY" streamlit run your-file-name.py

### Running a Streamlit App on Codespaces  
Follow these steps to launch and view your Streamlit app in GitHub Codespaces:
1. **Open the terminal** inside your Codespace.
2. Run the command:  
   ```bash
   streamlit run main.py
   ```  
 
3. After pressing **Enter**, a popup should appear in the bottom-right corner of Codespace editor.  
   - Click **“Open in Browser”** to view your app.  

   ⚠️ *If you miss the popup:*  
   - Press **Ctrl + C** in the terminal to stop the app.  
   - Rerun the command from step 2 — the popup should appear again.
4. A new browser tab will open, showing the interface of your Streamlit app.

