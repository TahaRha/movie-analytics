import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_articles(api_key, query, from_date, to_date, sort_by='publishedAt'):
    base_url = 'https://newsapi.org/v2/everything'
    articles = []

    params = {
        'apiKey': api_key,
        'q': query,
        'from': from_date,
        'to': to_date,
        'sortBy': sort_by,
        'pageSize': 100, #limit for account we have 
        'page': 1
    }

    while True:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print("Failed to fetch articles:", response.text)
            break

        data = response.json()
        articles.extend(data['articles'])

        if params['page'] * 100 >= data['totalResults']:
            break

        params['page'] += 1

    return articles

def main():
    api_key = input("Enter your NewsAPI key: ")
    query = '(Barbie AND movie)'  
    
    # Set the date range to the last 30 days
    to_date = datetime.today().strftime('%Y-%m-%d')
    from_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

    articles = fetch_articles(api_key, query, from_date, to_date)

    if articles:
        # Convert to DataFrame for easier manipulation
        df = pd.DataFrame(articles)
        print(df.head())

        # Save to CSV
        df.to_csv('barbie_movie_articles.csv', index=False)
        print("Articles saved to barbie_movie_articles.csv")
    else:
        print("No articles found.")

if __name__ == "__main__":
    main()
