import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer

articles_df = pd.read_json('data_parsed/all_articles_merged.json')
articles_df['text'].fillna('', inplace=True)

movies = articles_df['movie'].unique()

custom_stop_words = ['film', 'films', 'movie', 'like']

default_stop_words = TfidfVectorizer(stop_words="english").get_stop_words()

custom_stop_words = list(set(custom_stop_words + list(default_stop_words)))

top_words_per_movie = {}

for movie in movies:
    movie_articles = articles_df[articles_df['movie'] == movie]['text'].tolist()

    if movie == 'Barbie':
        new_custom_stop_words = custom_stop_words + ['barbie']

    elif movie == 'Oppenheimer':
        new_custom_stop_words = custom_stop_words + ['oppenheimer']
    
    elif movie == 'Mission Impossible':
        new_custom_stop_words = custom_stop_words + ['mission', 'impossible', 'dead', 'reckoning']

    vectorizer = TfidfVectorizer(max_features=1000, stop_words=new_custom_stop_words)
    tfidf_matrix = vectorizer.fit_transform(movie_articles)
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.sum(axis=0).A1

    words_tfidf = {word: score for word, score in zip(feature_names, scores)}
    sorted_words_tfidf = dict(sorted(words_tfidf.items(), key=lambda item: item[1], reverse=True))
    top_words = dict(list(sorted_words_tfidf.items())[:30])

    top_words_per_movie[movie] = top_words

with open("data_parsed/tfidf_movies_separate.json", 'w') as f:
    json.dump(top_words_per_movie, f, indent=4)
