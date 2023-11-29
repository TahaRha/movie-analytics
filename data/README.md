**Barbie Movie Articles - Data**  
--
_For now it's just preliminary data_

**Important**
- GNews
     - **Most Promising**
     - The current data:
       - Keywords: 'Barbie Movie', 'Margot Robbie', 'Barbie', 'Barbenheimer', 'Greta Gerwig'
       - Dates: 06/21/2023 - 08/21/2023 (got ~200 articles for each keyword, one month before release & one month after release)
       - Clean Up: Combined json files into one and removed duplicates

- Mediastack
  - Can change start date but end date can not pass 1 month after  
  - Only fetches 100 articles
  - The current data:
       - The dataset was compiled from multiple CSV files that cointained articles that searched 'Barbie movie' from consecutive date ranges starting from July 16, 2023, to August 26, 2023, with each file covering a period that extends one day further than the previous (i.e. 2023/07/16 - 2023/08/16, 2023/07/17-2023/08/17, etc...) - the reason for this was an attempt to get coverage 5 days before and 5 days after movie release. I then used a script to combine these CSV files into a single file (removing duplicates)
       - **Issue:**
         1. Articles seem to only range from August 16, 2023 to August 26, 2023 - I do not know why it's doing this
         2. Maybe we filter it to only include "legitimate" newssources cuz a good bunch of the entries look like fake news

- NewsApi
     - Only fetches data in the last month (either we stick with this API but choose a more recent movie that came out or we change APIs) 
     - Only fetches 100 articles
     - The current data in the github is from Oct 27 - Nov 27  
      
