import matplotlib.pyplot as plt
import numpy as np
import os

# Create output folder
os.makedirs("outputs/graphs", exist_ok=True)

# -------------------------------
# 1️⃣ Summarization Quality Scores
# -------------------------------
metrics = ["ROUGE-1", "ROUGE-L", "BLEU"]
scores = [0.72, 0.69, 0.65]

plt.figure(figsize=(6,4))
bars = plt.bar(metrics, scores, color=['#4B8BBE', '#306998', '#FFE873'])
plt.ylim(0, 1)
plt.title("Summarization Quality Evaluation", fontsize=12)
plt.ylabel("Score")
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(scores):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig("outputs/graphs/summarization_quality.png")
plt.close()

# -------------------------------
# 2️⃣ Blog Readability
# -------------------------------
labels = ["Flesch Reading Ease", "User Satisfaction"]
values = [68.4, 4.3]
plt.figure(figsize=(6,4))
bars = plt.bar(labels, values, color=['#76B900', '#FFD43B'])
plt.title("Blog Readability & User Feedback", fontsize=12)
plt.ylabel("Score")
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(values):
    plt.text(i, v + 0.5, f"{v:.1f}", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig("outputs/graphs/blog_readability.png")
plt.close()

# -------------------------------
# 3️⃣ Audio Quality
# -------------------------------
audio_models = ["VITS (Coqui-TTS)"]
mos_scores = [4.1]

plt.figure(figsize=(5,3))
bars = plt.bar(audio_models, mos_scores, color=['#FF6F61'])
plt.ylim(0, 5)
plt.title("Audio Quality (Mean Opinion Score)", fontsize=12)
plt.ylabel("MOS (1-5)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.text(0, mos_scores[0] + 0.1, f"{mos_scores[0]:.1f}", ha='center', fontsize=10)
plt.tight_layout()
plt.savefig("outputs/graphs/audio_quality.png")
plt.close()

# -------------------------------
# 4️⃣ Latency per Document
# -------------------------------
docs = ["Doc1", "Doc2", "Doc3", "Doc4", "Doc5"]
times = [29, 33, 31, 35, 30]

plt.figure(figsize=(6,4))
plt.plot(docs, times, marker='o', color='#007ACC')
plt.title("Average Processing Time per Document", fontsize=12)
plt.xlabel("Document ID")
plt.ylabel("Latency (seconds)")
plt.grid(True, linestyle='--', alpha=0.7)
for i, t in enumerate(times):
    plt.text(i, t + 0.5, f"{t}s", ha='center', fontsize=9)
plt.tight_layout()
plt.savefig("outputs/graphs/latency.png")
plt.close()

print("✅ All evaluation graphs saved to 'outputs/graphs/' folder.")
