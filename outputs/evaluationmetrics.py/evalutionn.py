import matplotlib.pyplot as plt
import numpy as np

# Data
papers = ['Joshy & Rajan (2022)', 'Radha (2024)', 'Javanmardi (2024)', 'Mahum (2025)', 'Kundacina (2025)', 'Proposed Project (2025)']
f1_scores = [90, 93, 95, 96, 92, 98]
auc_scores = [91, 94, 96, 97, 93, 99]
precision_scores = [89, 92, 94, 95, 91, 97]
recall_scores = [91, 94, 95, 96, 92, 98]

# X positions
x = np.arange(len(papers))
width = 0.2

# Plot setup
plt.figure(figsize=(10, 6))
plt.bar(x - 1.5*width, f1_scores, width, label='F1-Score', color='#1f77b4')
plt.bar(x - 0.5*width, auc_scores, width, label='AUC', color='#2ca02c')
plt.bar(x + 0.5*width, precision_scores, width, label='Precision', color='#d62728')
plt.bar(x + 1.5*width, recall_scores, width, label='Recall', color='#9467bd')

# Highlight proposed project in green
plt.bar(x[-1] - 1.5*width, f1_scores[-1], width, color='#32CD32', edgecolor='black', linewidth=1.5)
plt.bar(x[-1] - 0.5*width, auc_scores[-1], width, color='#32CD32', edgecolor='black', linewidth=1.5)
plt.bar(x[-1] + 0.5*width, precision_scores[-1], width, color='#32CD32', edgecolor='black', linewidth=1.5)
plt.bar(x[-1] + 1.5*width, recall_scores[-1], width, color='#32CD32', edgecolor='black', linewidth=1.5)

# Labels and styling
plt.xlabel('Research Papers', fontsize=12)
plt.ylabel('Metric Value (%)', fontsize=12)
plt.title('Comparison of Evaluation Metrics Across Studies and Proposed Project', fontsize=14, fontweight='bold')
plt.xticks(x, papers, rotation=25, ha='right')
plt.ylim(80, 100)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save as PNG
plt.tight_layout()
plt.savefig('Evaluation_Metrics_Comparison_Project.png', dpi=300)
plt.show()
