import re

def clean_text(text):
    """
    Cleans the extracted text by:
    - Removing extra whitespace
    - Removing special characters
    - Normalizing newlines
    """
    try:
        # Remove multiple spaces and tabs
        text = re.sub(r'\s+', ' ', text)
        
        # Remove unwanted special characters (keep basic punctuation)
        text = re.sub(r'[^A-Za-z0-9.,!?;:()\'\" \n]', '', text)
        
        # Normalize multiple newlines
        text = re.sub(r'\n+', '\n', text)
        
        # Strip leading/trailing whitespace
        text = text.strip()
        
        return text
    except Exception as e:
        print(f"⚠️ Text cleaning failed: {e}")
        return text
