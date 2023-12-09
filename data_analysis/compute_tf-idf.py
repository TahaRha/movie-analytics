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


    # Get title and text columns from DataFrame
    articles_text = articles_df['text'].tolist()

    # Create and fit the TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(articles_text)

    # Get feature names (words)
    feature_names = vectorizer.get_feature_names_out()

    # Convert the TF-IDF matrix for articles DataFrame into a readable format
    articles_tfidf_df = pd.DataFrame(tfidf_matrix[:len(articles_text)].toarray(), columns=feature_names)

    top_words_per_article = {}
    
    for i in range(len(articles_tfidf_df)):
        # Sort TF-IDF scores for each document
        sorted_tfidf_scores = articles_tfidf_df.iloc[i].sort_values(ascending=False)
        
        # Get the top 10 words and their TF-IDF scores for each article
        top_words = sorted_tfidf_scores.head(10).to_dict()
        
        # Use the article title as the key and assign the top words with scores as the value
        top_words_per_article[articles_df.loc[i, 'title']] = top_words

    # Output the dictionary as a JSON

    with open(path_to_output, 'w') as f:
        json.dump(top_words_per_article, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--articles', type=str, required=True, help='Path to articles JSON file')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Path to output CSV file')

    args = parser.parse_args()
    path_to_articles = args.articles
    path_to_output = args.output_file

    main(path_to_articles, path_to_output)




