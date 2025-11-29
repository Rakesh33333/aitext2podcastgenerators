from transformers import pipeline

# Initialize summarization pipeline (CPU-friendly)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=150, min_length=50):
    """
    Summarizes the given text to a concise version.
    Returns summarized text.
    """
    try:
        if not text.strip():
            return ""
        
        summary = summarizer(
            text, max_length=max_length, min_length=min_length, do_sample=False
        )[0]['summary_text']
        
        return summary
    
    except Exception as e:
        print(f"⚠️ Error in summarization: {e}")
        return text
