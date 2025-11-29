import os
import torch
import fitz
import re
from tkinter import Tk, filedialog
from transformers import pipeline
from docx import Document
from TTS.api import TTS
from pydub import AudioSegment
from tqdm import tqdm  # ✅ Progress bar

# ---------------------------
# Step 1: Device Configuration
# ---------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device set to use {device}")

# ---------------------------
# Step 2: Text Extraction
# ---------------------------
def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""

    if ext == ".pdf":
        doc = fitz.open(file_path)
        for page in doc:
            page_text = page.get_text("text")
            text += page_text or ""
        doc.close()

    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif ext == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        raise ValueError("❌ Unsupported file type! Use .txt, .pdf, or .docx only.")

    if not text.strip():
        raise ValueError("⚠️ File is empty or unreadable (possibly scanned or image-based PDF).")

    # 🧹 Clean excessive whitespace and newlines
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ---------------------------
# Step 3: Summarization (with progress bar)
# ---------------------------
def summarize_text(text):
    print("⏳ Summarizing text...")
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",
                          device=0 if torch.cuda.is_available() else -1)

    text = text.replace("\n", " ")

    if len(text.split()) < 80:
        return text

    chunks, current_chunk = [], ""
    max_chunk = 600
    for s in text.split(". "):
        if len(current_chunk) + len(s) <= max_chunk:
            current_chunk += s + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = s + ". "
    if current_chunk:
        chunks.append(current_chunk.strip())

    summary = ""
    print(f"🧩 Total chunks to summarize: {len(chunks)}\n")

    for chunk in tqdm(chunks, desc="Summarizing Progress", ncols=100):
        result = summarizer(chunk, max_length=200, min_length=80, do_sample=False)
        summary += result[0]["summary_text"] + " "

    return summary.strip()

# ---------------------------
# Step 4: Blog Generation
# ---------------------------
def generate_blog(summary):
    print("📝 Generating detailed blog post...")
    generator = pipeline("text-generation", model="gpt2")

    # ✅ Dynamic prompt – uses only your input summary, no predefined topics
    prompt = f"""
Write a detailed, human-like blog post based on the following summary:
{summary}

The blog should include:
- A catchy and relevant title
- An engaging introduction
- Clear sections or chapters with headings
- Real-life or relatable examples
- A meaningful conclusion
- A link to a related blog page at the end
- Sidebar-style navigation links

Make it sound natural, conversational, and contextually relevant to the input summary.
Avoid using any unrelated themes — stay focused only on what the summary describes.
"""

    output = generator(prompt, max_length=700, temperature=0.8, num_return_sequences=1)
    blog_text = output[0]["generated_text"]
    return blog_text

# ---------------------------
# Step 5: Conversational Podcast
# ---------------------------
def generate_conversational_podcast(blog_text):
    print("🎙️ Generating natural conversational podcast...")

    intro = "Welcome to our podcast! Today, we’re diving into an interesting topic and sharing some valuable insights."
    outro = "That’s all for today’s episode. Thanks for tuning in — stay curious, keep learning, and join us next time for another engaging conversation!"

    blog_lines = blog_text.split(". ")

    # create a natural male-female conversation flow
    script = [intro]
    for i, line in enumerate(blog_lines[:10]):  # use top 10 sentences
        if i % 2 == 0:
            script.append(f"🧔 rakesh : {line.strip()}.")
        else:
            script.append(f"👧 priya  : {line.strip()}.")

    script.append(outro)
    final_text = "\n".join(script)

    # Initialize TTS
    tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=False)
    combined = AudioSegment.silent(duration=500)

    # alternate male-female voices
    for i, line in enumerate(script):
        speaker = "p226" if i % 2 else "p335"  # p226=male, p335=female
        temp_file = f"temp_{i}.wav"
        tts.tts_to_file(text=line, speaker=speaker, file_path=temp_file)
        combined += AudioSegment.from_wav(temp_file) + AudioSegment.silent(duration=200)
        os.remove(temp_file)

    os.makedirs("outputs", exist_ok=True)
    output_path = "outputs/conversational_podcast.wav"
    combined.export(output_path, format="wav")

    print(f"🎧 Podcast saved at {output_path}")
    return final_text

# ---------------------------
# Step 6: Main Function (with File Picker)
# ---------------------------
def main():
    # 🗂 File picker dialog
    Tk().withdraw()
    file_path = filedialog.askopenfilename(
        title="Select your text, PDF, or Word file",
        filetypes=[("Supported files", "*.txt *.pdf *.docx")]
    )

    if not file_path:
        print("❌ No file selected. Exiting.")
        return

    # Extract textpython main.py

    text = extract_text(file_path)
    print("\n--- Extracted Text Preview ---")
    print(text[:500])
    print("\n--- End of Preview ---")

    # Summarize
    summary = summarize_text(text)
    print("\n✅ Summary Generated:\n")
    print(summary[:600])

    # Blog
    blog_text = generate_blog(summary)
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/blog_post.txt", "w", encoding="utf-8") as f:
        f.write(blog_text)
    print("\n📰 Blog (with summary) saved at → outputs/blog_post.txt")

    # Podcast
    podcast_script = generate_conversational_podcast(blog_text)
    print("\n🎤 Podcast Script Preview:\n", podcast_script[:600])

# ---------------------------
# Run the program
# ---------------------------
if __name__ == "__main__":
    main()

