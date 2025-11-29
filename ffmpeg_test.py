from pydub import AudioSegment
import subprocess
import os

# ✅ Set the correct FFmpeg path
ffmpeg_path = r"C:\Users\anupr\Downloads\ffmpeg-8.0-essentials_build\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

# 1️⃣ Check FFmpeg version
try:
    version = subprocess.run([ffmpeg_path, "-version"], capture_output=True, text=True, check=True)
    print("FFmpeg version:\n", version.stdout)
except FileNotFoundError:
    print("FFmpeg not found! Check the path.")
    exit()

# 2️⃣ Tell pydub to use this FFmpeg
AudioSegment.converter = ffmpeg_path

# 3️⃣ Example: convert an MP3 file to WAV
input_file = "example.mp3"   # replace with your file
output_file = "output.wav"

if os.path.exists(input_file):
    sound = AudioSegment.from_file(input_file)
    sound.export(output_file, format="wav")
    print(f"Audio converted successfully: {output_file}")
else:
    print(f"Input file not found: {input_file}")
