import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from newsapi import query_newsapi
import argparse
from time import sleep

def main():
    parser = argparse.ArgumentParser(description='Process a query with optional start and end dates.')

    parser.add_argument('api_key', type=str, help='The API key')
    parser.add_argument('query_file', type=str, help='File containing list of queries')
    parser.add_argument('-o', '--output', type=str, help='Output file path', required=True)
    parser.add_argument('--start_date', type=str, help='The start date in YYYY-MM-DD format', required=False)
    parser.add_argument('--end_date', type=str, help='The end date in YYYY-MM-DD format', required=False)
    
    args = parser.parse_args()
    
    with open(args.query_file,'r') as f:
        queries = f.read().split('\n')
    
    combine_files = [f"combine{i}.csv" for i in range(len(queries))]
    
    for i in range(len(queries)):
        sleep(1)
        query_newsapi(args.api_key, queries[i], combine_files[i], args.start_date, args.end_date)

    sleep(1)
    dataframes = [pd.read_csv(file) for file in combine_files]

    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df.to_csv(args.output, index=False)
    for file in combine_files:
        os.remove(file)
    
    

if __name__ == "__main__":
    main()
