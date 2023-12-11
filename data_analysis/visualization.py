import seaborn as sns
import matplotlib.pyplot as plt
import json

with open('data_parsed/tfidf_movies_separate.json', 'r') as f:
    data = json.load(f)

# Create subplots to display graphs side by side
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Loop through each movie and its TF-IDF scores to create a graph
for i, (movie, tfidf_scores) in enumerate(data.items()):
    # Sort TF-IDF scores in descending order
    sorted_tfidf = sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)[:20]  # Select top 10 words
    
    # Create a bar plot using Seaborn
    sns.barplot(x=[score[1] for score in sorted_tfidf], y=[score[0] for score in sorted_tfidf], palette='viridis', ax=axes[i])
    axes[i].set_title(movie)
    axes[i].set_xlabel("TF-IDF Score")
    axes[i].set_ylabel("Words")

plt.tight_layout()
plt.savefig('data_visualization/tfidf_movies_separate.png')
plt.show()