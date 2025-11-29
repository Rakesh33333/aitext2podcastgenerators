import os
from pdfminer.high_level import extract_text as pdf_extract_text
import docx

def extract_text(file_path):
    """
    Extracts text from .txt, .pdf, or .docx files.
    Returns extracted text as a string.
    """
    try:
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        
        if ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                
        elif ext == ".pdf":
            text = pdf_extract_text(file_path)
            
        elif ext == ".docx":
            doc = docx.Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            
        else:
            raise ValueError("Unsupported file format. Please use .txt, .pdf, or .docx")
        
        return text
    
    except Exception as e:
        print(f"⚠️ Text extraction failed: {e}")
        return ""
