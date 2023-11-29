import requests
import pandas as pd
from datetime import datetime, timedelta
import argparse

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

def query_newsapi(api_key, query, outfile, from_date=None, to_date=None):
        
#     api_key = input("Enter your NewsAPI key: ")
#     query = '(Barbie AND movie)'
    
    # Set the date range to the last 30 days if not inputed
    if not to_date:
        to_date = datetime.today().strftime('%Y-%m-%d')
        
    if not from_date:
        to_date_obj = datetime.strptime(to_date, '%Y-%m-%d')
        from_date = (to_date_obj - timedelta(days=30)).strftime('%Y-%m-%d')

    articles = fetch_articles(api_key, query, from_date, to_date)

    if articles:
        # Convert to DataFrame for easier manipulation
        df = pd.DataFrame(articles)
#         print(df.head())

        # Save to CSV
        df.to_csv(outfile, index=False)
        print(f"Articles saved to {outfile}, query = {query}")
        return True
    else:
        print("No articles found.")
        return False

def main():
    parser = argparse.ArgumentParser(description='Process a query with optional start and end dates.')

    parser.add_argument('api_key', type=str, help='The API key')
    parser.add_argument('query', type=str, help='The query string')
    parser.add_argument('-o', '--output', type=str, help='Output file path', required=True)
    parser.add_argument('--start_date', type=str, help='The start date in YYYY-MM-DD format', required=False)
    parser.add_argument('--end_date', type=str, help='The end date in YYYY-MM-DD format', required=False)
    
    args = parser.parse_args()
    query_newsapi(args.api_key, args.query, args.output, args.start_date, args.end_date)

if __name__ == "__main__":
    main()
