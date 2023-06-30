import snscrape.modules.twitter as sntwitter
from pymongo import MongoClient
from datetime import datetime

def store_data_in_mongodb(mycollection, keyword, data):
    client = MongoClient()
    db = client['tweet']
    collection = db[mycollection]
    collection.insert_one({f'{keyword}+{datetime.now()}': data})
    client.close()


def scrape_twitter_data(keyword, start_date, end_date, tweet_count):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(f'{keyword} since:{start_date} until:{end_date}').get_items():
        if len(tweets) >= tweet_count:
            break
        tweets.append({
            'date': tweet.date,
            'id': tweet.id,
            'url': tweet.url,
            'content': tweet.content,
            'user': tweet.user.username,
            'reply_count': tweet.replyCount,
            'retweet_count': tweet.retweetCount,
            'language': tweet.lang,
            'source': tweet.source,
            'like_count': tweet.likeCount
        })
    return tweets
import streamlit as st
import pandas as pd

# Define Streamlit app layout and input fields
st.title("Twitter Data Scraper")
keyword = st.text_input("Enter a keyword or hashtag")
start_date = st.date_input("Start date")
end_date = st.date_input("End date")
tweet_count = st.number_input("Tweet count", value=100)

# Scrape Twitter data on button click
if st.button("Scrape"):
    scraped_data = scrape_twitter_data(keyword, start_date, end_date, tweet_count)
    df = pd.DataFrame(scraped_data)
    st.write(df)

# Store data in MongoDB on button click
if st.button("Upload to MongoDB"):
    store_data_in_mongodb(f'LIC corporation+{datetime.now()}', keyword, scraped_data)
    st.success("Data uploaded to MongoDB!")

# Download data in CSV and JSON formats
if st.button("Download CSV"):
    df.to_csv("twitter_data.csv", index=False)
    st.success("CSV file downloaded!")

if st.button("Download JSON"):
    df.to_json("twitter_data.json", orient="records")
    st.success("JSON file downloaded!")
