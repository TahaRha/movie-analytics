import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import json

with open('data_parsed/categories_sentiments.json', 'r') as f:
    sentiment_data = json.load(f)

formatted_data = []
for category, values in sentiment_data.items():
    for movie, sentiment in values.items():
        formatted_data.append({'Category': category, 'Movie': movie, 'Sentiment': sentiment})

# Create a DataFrame from the formatted data
df = pd.DataFrame(formatted_data)

# Create a grouped bar plot using Seaborn
plt.figure(figsize=(12, 8))
sns.barplot(x='Category', y='Sentiment', hue='Movie', data=df, palette='muted', dodge=True)
plt.title('Sentiment Comparison across Categories for Movies')
plt.xlabel('Categories')
plt.ylabel('Sentiment')
plt.xticks(rotation=45, ha='right')  # Adjust rotation and alignment of x-axis labels
plt.legend(title='Movie', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('data_visualization/sentiment_categories.png')
plt.show()