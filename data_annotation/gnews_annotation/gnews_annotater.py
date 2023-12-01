import json
import random

# Load the JSON file
with open('gnews_barbie_movie_articles.json', 'r', encoding='utf-8') as file:
    articles = json.load(file)

# Define keywords for each category
category_keywords = {
    "Box Office Performance and Industry Impact": ["box office", "sales", "grossing", "financial", "industry impact", "ticket sales", "revenue", "economic", "market", "record-breaking", "earnings"],
    "Cultural and Social Commentary": ["cultural", "social impact", "gender roles", "feminism", "representation", "diversity", "social norms", "influence", "identity", "societal", "empowerment"],
    "Behind-the-Scenes and Production Insights": ["Greta Gerwig", "behind-the-scenes", "production", "filming", "director", "cast interviews", "making of", "set design", "shooting", "cinematography", "screenplay", "script"],
    "Fashion and Aesthetics": ["fashion", "costumes", "design", "style", "aesthetics", "Barbie Pink", "wardrobe", "outfits", "makeup", "visual style", "art direction"],
    "Celebrity and Cast Focus": ["Margot Robbie", "Ryan Gosling", "cast", "actor", "actress", "celebrity", "interview", "performance", "star", "cast insights"],
    "Marketing and Promotional Strategies": ["marketing", "promotion", "advertising", "campaign", "trailer", "merchandise", "PR", "public relations", "branding", "launch", "premiere"],
    "Fan and Audience Reactions": ["fans", "audience", "reaction", "reviews", "social media", "memes", "hashtags", "trending", "viewership", "audience response", "feedback", "TikTok", "Twitter", "Instagram", "Facebook"],
    "Critique and Reviews": ["review", "critique", "analysis", "rating", "criticism", "opinion", "film review", "movie critique", "reception", "critical", "commentary"],
    "Merchandise and Commercial Tie-Ins": ["merchandise", "toys", "product", "commercial", "tie-in", "retail", "sales", "Barbie doll", "collectibles", "brand partnership", "licensed"],
    "Global and Political Perspectives": ["global", "international", "political", "controversy", "ban", "censorship", "cross-cultural", "diplomacy", "worldwide", "geopolitical", "policy"]
}

# Function to categorize articles
def categorize_article(article, category_keywords):
    title = article['title'].lower()
    description = article.get('description', '').lower()
    text = title + " " + description

    for category, keywords in category_keywords.items():
        if any(keyword in text for keyword in keywords):
            return category
    return "Uncategorized"

# Separate categorized and uncategorized articles
categorized_articles = []
uncategorized_articles = []

for article in articles:
    category = categorize_article(article, category_keywords)
    article['category'] = category

    if category == "Uncategorized":
        uncategorized_articles.append(article)
    else:
        categorized_articles.append(article)

# Save categorized articles
with open('Barbie_categorized_articles.json', 'w') as file:
    json.dump(categorized_articles, file)

# Save uncategorized articles
with open('Barbie_uncategorized_articles.json', 'w') as file:
    json.dump(uncategorized_articles, file)
