import streamlit as st
from file_loader import extract_text_from_file
from qa_engine import get_top_k_chunks, get_answer_from_gemini
import io

# Page setup
st.set_page_config(page_title="RAG Chatbot with Gemini", layout="wide")
st.title("📄 RAG-powered Document Chatbot")
st.write("Upload a document (PDF, DOCX, TXT) and ask questions about its content.")

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'document_text' not in st.session_state:
    st.session_state.document_text = ""
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# Clear chat + document button
if st.button("🗑️ Clear Chat History & Document"):
    st.session_state.chat_history = []
    st.session_state.document_text = ""
    st.session_state.uploaded_file = None
    st.success("Chat history and uploaded document cleared!")

# File uploader
uploaded_file = st.file_uploader("Upload your document here", type=["pdf", "docx", "txt"])
if uploaded_file:
    st.session_state.uploaded_file = uploaded_file
    st.session_state.document_text = extract_text_from_file(uploaded_file)
    st.success("✅ Document uploaded and text extracted!")

# Text input for question
user_question = st.text_input("Ask a question about the document:")

# Run RAG + Gemini QA
if st.session_state.document_text and user_question:
    top_chunks = get_top_k_chunks(st.session_state.document_text, user_question)
    answer = get_answer_from_gemini(top_chunks, user_question)

    # Store in chat history
    st.session_state.chat_history.append({
        "question": user_question,
        "answer": answer
    })

    st.subheader("🧠 Bot's Response")
    st.markdown(answer)

# Show chat history
if st.session_state.chat_history:
    st.subheader("🗂️ Chat History")
    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {chat['question']}")
        st.markdown(f"**Bot:** {chat['answer']}")
        st.markdown("---")

    # Add download chat history button
    chat_content = "\n\n".join([f"You: {c['question']}\nBot: {c['answer']}" for c in st.session_state.chat_history])
    buffer = io.StringIO(chat_content)
    st.download_button(
        label="⬇️ Download Chat History as TXT",
        data=buffer.getvalue(),
        file_name="chat_history.txt",
        mime="text/plain"
    )
