# Twitter_Scraping
python scripting, Data Collection, MongoDB, Streamlit

![Twitter-Scraper jpg](https://github.com/ThirumuruganMasilamani/Twitter_Scraping/assets/128259902/2507791d-0635-4a89-9ae6-28545ed5ff56)


By using the “snscrape” Library, Scrape the twitter data from Twitter. Create a dataframe with date, id, url, tweet content, user,reply count, retweet count,language, source, like count. Store each collection of data into a document into Mongodb along with the hashtag or key word we use to Scrape from twitter. eg:({“LIC corporation+current Timestamp”: [{1000 Scraped data from past 100 days }]}) Create a GUI using streamlit that should contain the feature to enter the keyword or Hashtag to be searched, select the date range and limit the tweet count need to be scraped. After scraping, the data needs to be displayed in the page and need a button to upload the data into Database and download the data into csv and json format.

## Features

- Scrape Twitter data using the `snscrape` library.
- Extract the following fields from each tweet: date, id, URL, tweet content, user, reply count, retweet count, language, source, and like count.
- Store the scraped data in a pandas DataFrame.
- Store each collection of data into a document in MongoDB, along with the hashtag or keyword used for scraping.
- Create a Streamlit GUI with the following features:
- Input field to enter the keyword or hashtag to be searched.
- Date range selection to specify the start and end dates for the data scraping.
- Option to limit the number of tweets to be scraped.
- Display the scraped data in a table on the app's page.
- Button to upload the data to MongoDB.
- Buttons to download the data in CSV and JSON formats.

## Final Output
![Twitter-Scraping Op](https://github.com/ThirumuruganMasilamani/Twitter_Scraping/assets/128259902/dcc9b770-35ea-4ebc-bc9a-dcddb11ab7ac)
