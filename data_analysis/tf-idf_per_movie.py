import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import argparse

articles_df = pd.read_json('data_parsed/all_articles_merged.json')
# Drop rows with NaN values
articles_df['text'].fillna('', inplace=True)

top_words_per_movie = {}

grouped_articles = articles_df.groupby('movie')

for movie, group in grouped_articles:
    combined_text = ' '.join(group['text'].tolist())

    # Create and fit the TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([combined_text])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]

    # Create a dictionary of words and their TF-IDF scores
    words_tfidf = {word: score for word, score in zip(feature_names, scores)}

    # Sort the dictionary by TF-IDF scores
    sorted_words_tfidf = dict(sorted(words_tfidf.items(), key=lambda item: item[1], reverse=True))

    # Get the top 20 words and their TF-IDF scores for each movie
    top_words = dict(list(sorted_words_tfidf.items())[:30])

    # Use the movie as the key and assign the top words with scores as the value
    top_words_per_movie[movie] = top_words

# Output the dictionary as a JSON
with open("data_parsed/tfidf_movies.json", 'w') as f:
    json.dump(top_words_per_movie, f, indent=4)