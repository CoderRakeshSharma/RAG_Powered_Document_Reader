# 📄 RAG-Powered Document Chatbot with Gemini  

This project is a **smart chatbot** that can read your **PDF, DOCX, or TXT** documents and answer any questions about their content.  

It uses a **Retrieval-Augmented Generation (RAG)** approach with **Google Gemini AI**, meaning it first finds the most relevant text from your document and then asks Gemini to answer your question in a natural way.  

Even a child can think of it like this:  
- 🏫 **Imagine you give your teacher a book (your document)**  
- 🙋 **You ask the teacher a question about the book**  
- 🧠 **The teacher looks at the book, finds the right part, and then explains the answer to you clearly**  

That’s exactly what this chatbot does!  

---

## ✨ Features  

✅ Upload **PDF, DOCX, or TXT** files  
✅ Ask questions in **normal language**  
✅ Uses **smart AI (Gemini)** to find answers  
✅ Keeps a **chat history** so you can see all past questions and answers  
✅ **Clear chat & document** anytime  
✅ **Download chat history** as TXT  

---

## 📦 Installation  

1️⃣ **Clone this project**  

```bash
git clone <your-repo-url>
cd RAG_Powered_Document_Reader
```

2️⃣ **Create a virtual environment & activate it**  

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3️⃣ **Install required dependencies**  

```bash
pip install streamlit PyPDF2 python-docx sentence-transformers google-generativeai
```

---

## 🚀 How to Run  

1️⃣ **Set your Gemini API key**  

In your terminal:  
```bash
set GOOGLE_API_KEY=your_api_key_here  # Windows
export GOOGLE_API_KEY=your_api_key_here  # macOS/Linux
```

2️⃣ **Run the Streamlit app**  

```bash
streamlit run rag_chatbot.py
```

3️⃣ **Open your browser**  
Go to **http://localhost:8501**  

---

## 🏗️ How It Works  

1. **Extract text** → When you upload a document, the app extracts all the text.  
2. **Find best matches** → When you ask a question, it finds the most relevant parts.  
3. **Ask Gemini** → It sends the relevant text + your question to **Google Gemini AI**.  
4. **Show answer** → Gemini gives a nice, simple answer.  

---

## 📁 Project Structure  

```
📂 RAG_Powered_Document_Reader
 ├── rag_chatbot.py        # Main Streamlit app
 ├── file_loader.py        # Extracts text from PDF/DOCX/TXT
 ├── qa_engine.py          # Handles embeddings + Gemini QA
 ├── requirements.txt      # Dependencies list
 ├── .gitignore            # Ignore unnecessary files
 └── README.md             # This file
```

---

## 🖱️ How to Use  

1️⃣ Upload any **PDF/DOCX/TXT** document  
2️⃣ Type your question in the text box  
3️⃣ The chatbot will **read your document & answer**  
4️⃣ You can **clear chat + document anytime**  
5️⃣ You can **download chat history** as TXT  

---

## 🎯 Example  

- You upload a **Company Policy PDF**  
- You ask:  
  > *“What is the company’s leave policy?”*  
- The chatbot finds the right section and answers:  
  > *“The company allows 20 paid leaves per year and requires 2 days prior notice.”*  

---

## 🛠️ Tech Used  

- **Streamlit** → Web app interface  
- **PyPDF2 / python-docx** → Extract text from documents  
- **SentenceTransformers** → Find most relevant text chunks  
- **Google Gemini AI** → Generate natural answers  

---

## 📜 License  

This project is free to use for learning purposes.  

---

**Now you can ask your documents anything, just like chatting with a super-smart friend! 🚀**  

