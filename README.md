# Stock Sentiment Analysis System

## Overview
Welcome to the Stock Sentiment Analysis System repository! This Python project is designed to analyze the sentiment of financial news related to specific stocks. The system gathers data from FINVIZ, performs sentiment analysis using NLTK's Vader SentimentIntensityAnalyzer, and visualizes the results through a bar chart.

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
