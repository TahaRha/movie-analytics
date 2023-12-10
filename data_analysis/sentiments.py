import pandas as pd
from textblob import TextBlob
import json

with open('data_parsed/all_articles_merged.json', 'r') as f:
    data = json.load(f)

articles_df = pd.DataFrame(data)

# Drop rows with NaN values in 'text' column and floats
articles_df = articles_df.dropna(subset=['text'])
articles_df = articles_df[articles_df['text'].apply(lambda x: isinstance(x, str))]

# Function to get sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Apply sentiment analysis to each group (category and movie)
sentiments = articles_df.groupby(['category', 'movie'])['text'].apply(lambda x: x.apply(get_sentiment).mean()).reset_index()

# Rename the column with sentiment scores
sentiments = sentiments.rename(columns={'text': 'sentiment'})

categories_sentiments = {}

for category in sentiments['category'].unique():
    categories_sentiments[category] = {}
    for movie in sentiments[sentiments['category'] == category]['movie'].unique():
        categories_sentiments[category][movie] = sentiments[(sentiments['category'] == category) & (sentiments['movie'] == movie)]['sentiment'].values[0]

with open('data_parsed/categories_sentiments.json', 'w') as f:
    json.dump(categories_sentiments, f, indent=4)

