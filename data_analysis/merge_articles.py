import json



# Load each JSON file
with open('data_parsed/barbie_with_text.json', 'r', encoding='utf-8') as barbie_file:
    barbie_data = json.load(barbie_file)
    barbie_data = [{'movie': 'Barbie', **article} for article in barbie_data]

with open('data_parsed/oppie_with_text.json', 'r', encoding='utf-8') as oppie_file:
    oppie_data = json.load(oppie_file)
    oppie_data = [{'movie': 'Oppenheimer', **article} for article in oppie_data]

with open('data_parsed/mi_with_text.json', 'r', encoding='utf-8') as mission_impossible_file:
    mission_impossible_data = json.load(mission_impossible_file)
    mission_impossible_data = [{'movie': 'Mission Impossible', **article} for article in mission_impossible_data]

# Concatenate articles from all three movies
all_articles = barbie_data + oppie_data + mission_impossible_data

print(len(all_articles))

# Write the merged articles to a new JSON file
with open('data_parsed/all_articles_merged.json', 'w') as merged_file:
    json.dump(all_articles, merged_file, indent=2)
