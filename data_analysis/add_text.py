from gnews import GNews
import json
import argparse

def main(input_file, output_file):
    # Read in articles from JSON file
    with open(input_file, 'r', encoding='utf-8') as file:
        articles = json.load(file)

    # Initialize GNews
    google_news = GNews()

    # Iterate through each article and add a 'text' field
    for article in articles:
        url = article['url']
        try:
            # Get full article using gnews.get_full_article
            full_article = google_news.get_full_article(url)
            
            if full_article and hasattr(full_article, 'text'):
                article['text'] = full_article.text
            else:
                print(f"Could not extract text from article at {url}")
        except Exception as e:
            print(f"Error processing article at {url}: {e}")

    # Write updated articles to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(articles, file, ensure_ascii=False, indent=4)

    print(f"Updated articles saved to {output_file}")

# Run the script
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input_file', type=str, required=True, help='Path to input JSON file')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Path to output JSON file')

    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    main(input_file, output_file)
