# Stock Sentiment Analysis

# Import required libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import datetime

# STEP 1 : GET THE DATA
#-----------------------

# Base url to finviz site
finviz_url = 'https://finviz.com/quote.ashx?t='

# Read in user defined stock tickers from txt file
ticker_file = open("tickers.txt", "r")
tickers = ticker_file.read().splitlines()
tickers.pop(0)

# Pull each stocks relevant information
news_tables = {}
for stock in tickers:
    # Append the ticker onto the base URL
    url = finviz_url + stock
    # Create a request object for the url
    req = Request(url=url, headers={'user-agent': 'my-app'})
    # Send the request and open the response
    res = urlopen(req)
    # Parse the response data as html
    html = BeautifulSoup(res, 'html')
    # Pull the "news-table" id component from the html
    news_table = html.find(id="news-table")
    news_tables[stock] = news_table

# STEP 2 : PARSE, MANIPULATE AND CLEAN THE DATA
#-----------------------------------------------

# Pull each articles stock, date, time and title

# Declare list to store cleaned data
clean_data = []
for stock, news_table in news_tables.items():

    # Grab each article for a given stock and store it's date, time and title
    for line in news_table.findAll('tr'):

        # Title is stored in an a-tag
        title = line.a.text
        # Date info is in td component
        date_info = line.td.text.split(' ')
        # Remove white spaces in the split output
        date_info[:] = [x for x in date_info if x]

        # Not all articles have a date as the site groups dates, hence we must handle this
        if len(date_info) == 2:
            time = date_info[1]
        else:
            time = date_info[2]
            date = date_info[1] if date_info[1] != 'Today' else datetime.date.today()

        clean_data.append([stock, date, time, title])


# STEP 3 : APPLYING SENTIMENT ANALYSIS
#--------------------------------------

# NLTK Background Iformation:
# Natural Language Toolkit (NLTK) is a Python library for natural language processing.
# NLTK's SentimentIntensityAnalyzer provides a compound score (-1 to 1) for sentiment analysis.
# Higher values indicate more positive sentiment, lower values more negative, and around 0 is neutral.

# Create pandas data frame
df = pd.DataFrame(clean_data, columns=['stock', 'date', 'time', 'title'])
# Initialise nltk sentiment analyser object
vader = SentimentIntensityAnalyzer()

# Function to take the title as input and return the compounded sentiment score
def getSentiment(title):
    return vader.polarity_scores(title)['compound']

# Add the sentiment results as it's own column in the data frame
df['sentiment'] = df['title'].apply(getSentiment)

# STEP 4 : VISUALISING THE DATA
#--------------------------------

# Re-format the date column to present as a datetime object
df['date'] = pd.to_datetime(df.date, format="mixed").dt.date

# Calculate the mean sentiment score for a given stock on a given date
mean_df = df.groupby(['stock', 'date'])['sentiment'].mean()
# Re-format the data frame in preperation for the plot
mean_df = mean_df.unstack()
mean_df = mean_df.transpose()

# Plot the data
mean_df.plot(kind = 'bar')
plt.show()

