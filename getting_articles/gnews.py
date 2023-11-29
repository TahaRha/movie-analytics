import json
from gnews import GNews

# Initialize GNews - change start_date + end_date to whenever
google_news = GNews(language='en', country='US', start_date=(2023, 7, 21), end_date=(2023, 8, 21), max_results=500)

# Fetch articles for keywords - here I was trying barbenheimer
articles = google_news.get_news('barbenheimer')

# JSON file setup
json_file = "gnews_barbenheimer_articles.json"

# Write to JSON
try:
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(articles, file, ensure_ascii=False, indent=4)
except IOError:
    print("I/O error while writing to JSON")

print(f"{len(articles)} articles saved to {json_file}")
