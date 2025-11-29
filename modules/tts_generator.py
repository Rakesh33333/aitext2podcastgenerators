from TTS.api import TTS
import os

def generate_podcast(text, lang="en", voice_type="female"):
    """
    Generate podcast audio using Coqui TTS with natural male/female voices.
    Supports English and multiple other languages.
    """

    try:
        os.makedirs("outputs", exist_ok=True)

        # Select a model based on language and gender
        if lang.startswith("en"):
            if voice_type.lower() == "male":
                model_name = "tts_models/en/vctk/vits"
                speaker = "p226"  # male
            else:
                model_name = "tts_models/en/vctk/vits"
                speaker = "p240"  # female
        elif lang.startswith("hi"):  # Hindi
            model_name = "tts_models/hi/cv/vits"
            speaker = None
        elif lang.startswith("es"):  # Spanish
            model_name = "tts_models/es/css10/vits"
            speaker = None
        else:
            model_name = "tts_models/multilingual/multi-dataset/your_tts"
            speaker = None

        print(f"🎙️ Using model: {model_name} | Speaker: {speaker or 'default'}")

        # Load TTS model
        tts = TTS(model_name)

        # Output path
        output_path = "outputs/final_podcast.mp3"

        # Generate speech
        if speaker:
            tts.tts_to_file(text=text, file_path=output_path, speaker=speaker)
        else:
            tts.tts_to_file(text=text, file_path=output_path)

        print(f"✅ Podcast saved successfully → {output_path}")

    except Exception as e:
        print(f"⚠️ Error during TTS generation: {e}")
