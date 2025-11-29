from langdetect import detect
from deep_translator import GoogleTranslator

def translate_to_english(text):
    """Detect language and translate to English if needed."""
    try:
        lang = detect(text)
        if lang != 'en':
            print(f"🌐 Detected language: {lang} → Translating to English...")
            translated = GoogleTranslator(source='auto', target='en').translate(text)
            return translated
        else:
            print("🌐 Language is English → No translation needed.")
            return text
    except Exception as e:
        print(f"⚠️ Translation failed: {e}")
        return text
