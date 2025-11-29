import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get all available voices
voices = engine.getProperty('voices')

print("🎙️ Available Voices on Your System:\n")
for index, voice in enumerate(voices):
    print(f"{index+1}. Name: {voice.name}")
    print(f"   ID: {voice.id}")
    print(f"   Languages: {voice.languages}")
    print("--------------------------------------------------")

# Test voice generation
if len(voices) == 0:
    print("❌ No voices found. Please install Microsoft Speech voices (e.g., David, Zira).")
else:
    # Use first voice as male
    print("\n🔊 Generating male voice test...")
    engine.setProperty('voice', voices[0].id)
    engine.save_to_file("Hello! This is the male voice test. How are you today?", "male_test.mp3")

    # If at least two voices exist, use second as female
    if len(voices) > 1:
        print("🔊 Generating female voice test...")
        engine.setProperty('voice', voices[1].id)
        engine.save_to_file("Hi there! This is the female voice test. I’m doing great, thank you!", "female_test.mp3")
    else:
        print("⚠️ Only one voice found. Female test will be skipped.")

    engine.runAndWait()

print("\n✅ Test complete! Check the following files in your folder:")
print("   - male_test.mp3")
print("   - female_test.mp3 (if two voices were found)")
print("\n🎯 Note down the 'Name' or 'ID' for male and female voices.")
print("   You’ll use them inside modules/tts_generator.py like this:")
print('   male_voice_name = "David"')
print('   female_voice_name = "Zira"')
