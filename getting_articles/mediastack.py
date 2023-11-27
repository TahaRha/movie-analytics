import requests
import pandas as pd

def fetch_articles(api_key, query, from_date, to_date):
    base_url = 'http://api.mediastack.com/v1/news'
    articles = []

    params = {
        'access_key': api_key,
        'keywords': query,
        'languages': 'en',  
        'date': f"{from_date},{to_date}",
        'sort': 'published_desc',  # Sorting by most recently published
        'limit': 100
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles.extend(data['data'])
    else:
        print("Failed to fetch articles:", response.text)

    return articles

def main():
    api_key = input("Enter your Mediastack API key: ")
    query = 'Barbie movie'
    
    # from movie's release date in Canada to a month later (this is all the API can handle)
    from_date = '2023-07-21'
    to_date = '2023-08-21'  

    articles = fetch_articles(api_key, query, from_date, to_date)

    if articles:
        # Convert to DataFrame 
        df = pd.DataFrame(articles)
        print(df.head())

        # Save to CSV
        df.to_csv('barbie_movie_articles_mediastack.csv', index=False)
        print("Articles saved to barbie_movie_articles_mediastack.csv")
    else:
        print("No articles found.")

if __name__ == "__main__":
    main()
