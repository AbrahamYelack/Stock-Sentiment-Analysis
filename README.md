# Stock Sentiment Analysis

## Overview
This Python project is designed to analyze the sentiment of financial news related to specific stocks. The system gathers data from FINVIZ, performs sentiment analysis using NLTK's Vader SentimentIntensityAnalyzer, and visualizes the results through a bar chart.

Sentiment stock analysis is highly valuable in the contemporary financial landscape, as it taps into the influence of information technologies and social media on market dynamics. In today's interconnected world, where news and opinions spread rapidly, sentiment analysis goes beyond traditional financial metrics by evaluating emotional tones and expressions in online platforms. By deciphering market sentiment from social media, financial news, and online forums, investors gain insights into collective moods, potential shifts in sentiment, and early signs of market trends. This approach provides a dynamic perspective, enabling market participants to make more informed and adaptive trading decisions, making sentiment stock analysis an indispensable tool in navigating the fast-paced and interconnected nature of modern financial markets.

## Prerequisites
Make sure you have the required libraries installed:
- beautifulsoup4
- pandas
- nltk
- matplotlib

## Usage
Create a text file named tickers.txt and list the stock tickers you want to analyze, one per line.
Run the provided Python script.

## How It Works
Sentiment analysis is conducted using NLTK's Vader SentimentIntensityAnalyzer, which assigns compound scores to text data. Positive, neutral, and negative sentiments are identified based on these scores.

## Identifying Positive and Negative Sentiments:

Compound scores above 0.2 are considered positive.
Compound scores below -0.2 are considered negative.
Applying Sentiment to Stocks:

Sentiment scores are calculated for financial news headlines related to specific stocks.
Mean sentiment scores are computed for each stock on a given date.
Feel free to customize the code according to your needs and explore further enhancements.
