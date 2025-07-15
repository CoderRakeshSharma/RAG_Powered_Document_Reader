import PyPDF2
import docx2txt

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1].lower()

    if file_type == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_type == 'docx':
        return docx2txt.process(uploaded_file)
    elif file_type == 'txt':
        return uploaded_file.read().decode('utf-8')
    else:
        return "Unsupported file type."

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
