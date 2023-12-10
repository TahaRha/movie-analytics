import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import argparse

def main(path_to_articles, path_to_output):
    articles_df = pd.read_json(path_to_articles)
    # Drop rows with NaN values
    articles_df['text'].fillna('', inplace=True)

    top_words_per_category = {}

    grouped_articles = articles_df.groupby('category')

    for category, group in grouped_articles:
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

        # Get the top 10 words and their TF-IDF scores for each category
        top_words = dict(list(sorted_words_tfidf.items())[:10])

        # Use the category as the key and assign the top words with scores as the value
        top_words_per_category[category] = top_words

    # Output the dictionary as a JSON
    with open(path_to_output, 'w') as f:
        json.dump(top_words_per_category, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--articles', type=str, required=True, help='Path to articles JSON file')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Path to output CSV file')

    args = parser.parse_args()
    path_to_articles = args.articles
    path_to_output = args.output_file

    main(path_to_articles, path_to_output)



